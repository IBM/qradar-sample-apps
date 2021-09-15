# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import os
from flask import Blueprint, render_template, request, redirect
from requests.exceptions import SSLError
from werkzeug.utils import secure_filename
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')

CERTS_DIRECTORY = '/opt/app-root/store/certs'


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    cert_app = get_certificate_management_app()
    url = request.args.get('address')
    if url is not None:
        try:
            response = requests.get(url)
        except SSLError as ssl_error:
            return render_template('index.html',
                                   url=url,
                                   result='An SSL error occurred!', 
                                   status_code = str(ssl_error),
                                   cert_app=cert_app)                 
        return render_template('index.html',
                               url=url, 
                               status_code=response.status_code,
                               result=response.text, cert_app=cert_app
                               )
    return render_template('index.html', cert_app=cert_app)


@viewsbp.route('/upload_cert', methods=['POST'])
def upload_cert():
    if 'cert' not in request.files:
        qpylib.log('no certificate file in upload request')
        return redirect('/', code=303)
    file = request.files['cert']
    # If the user does not select a file, the browser also submits an empty part without filename
    if file.filename == '':
        qpylib.log('no certificate file in upload request')
        return redirect('/', code=303)
    filename = secure_filename(file.filename)
    file.save(os.path.join(CERTS_DIRECTORY, filename))
    refresh_certs()
    return redirect('/', code=303)

def get_certificate_management_app():
    params = {'filter': 'manifest(name)="QRadar Certificate Management" and application_state(status)="RUNNING"',
              'fields': 'application_state'}
    response = qpylib.REST(rest_action='GET',
                            request_url='/api/gui_app_framework/applications',
                            params=params)
    if not response.status_code == 200:
        qpylib.log('Failed to get Certificate Management App')
    jsonResult = response.json()
    address=""
    if len(jsonResult) > 0:
        for app_id in jsonResult:
            cert_management_id = app_id['application_state']['application_id']
        console_ip = qpylib.get_console_address()
        address = "https://{0}/console/plugins/{1}/app_proxy/#/browse/uploadRoot".format(console_ip, cert_management_id)
    return address

def refresh_certs():
    os.system('sudo /opt/app-root/bin/update_ca_bundle.sh')

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
    url = request.args.get('address')
    if url is not None:
        try:
            response = requests.get(url)
        except SSLError:
            return render_template('index.html',
                                   url=url,
                                   result='An SSL error occurred!')
        return render_template('index.html',
                               url=url,
                               status_code=response.status_code,
                               result=response.text)
    return render_template('index.html')


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


def refresh_certs():
    os.system('sudo /opt/app-root/bin/update_ca_bundle.sh')

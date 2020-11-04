# Copyright 2020 IBM Corporation

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import requests
from flask import Blueprint, render_template

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# Endpoint that fetches QRadar proxy settings if they are set, before making
# an HTTP request manually using these proxy settings to X-Force Exchange and
# displaying the results to the user injected into the HTML template.
# If no proxy settings are set an error is shown explaining that no proxy
# settings have been set.
@viewsbp.route('/index')
def index():
    if 'QRADAR_HTTPS_PROXY' in os.environ:
        # Manually retrieve QRadar proxy values
        qradar_https_proxy = os.environ.get('QRADAR_HTTPS_PROXY')
        qradar_http_proxy = os.environ.get('QRADAR_HTTP_PROXY')
        qradar_no_proxy = os.environ.get('QRADAR_NO_PROXY')

        # Make HTTP request using proxy values to IBM X-Force Exchange to get
        # the download count for the QRadar Assistant app
        # NOTE: This manual proxy set up is not the recommended way to do this,
        # QRadar sets the python http_proxy and https_proxy values
        # automatically, meaning that it is handled automatically and this
        # manual setup is not needed - it is only to demo how to manually
        # use the proxy values
        proxies = {
            'http': qradar_http_proxy,
            'https': qradar_https_proxy,
        }
        response = requests.get(
            'https://api.xforce.ibmcloud.com/hub/extensions/ed8aee4440f98f9c8bedaff4c5c644de',
            proxies=proxies)
        assistant_info = response.json()
        download_count = assistant_info["extensions"][0]["downloads"]

        return render_template('index.html',
                               proxy_set=True,
                               qradar_https_proxy=qradar_https_proxy,
                               qradar_http_proxy=qradar_http_proxy,
                               qradar_no_proxy=qradar_no_proxy,
                               download_count=download_count)
    return render_template('index.html', proxy_set=False)

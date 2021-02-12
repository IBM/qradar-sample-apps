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

from flask import Blueprint, render_template, request
import json

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    return render_template("index.html", title="MultiComponent App!")


@viewsbp.route('/sampleIpInformation')
def sample_ip_info():

    ip = request.args.get('metaDataContext')
    map_location = "https://www.iptrackeronline.com/locate-ip-on-map.php"

    return json.dumps({
        "key": "sampleIPInfo",
        "label": "Sample IP Information",
        "html": """
        <form style='display:none' method=POST target='ipMapFrame' id='ipMap' action='"""
                + map_location + """'>
        <input name=ip value='""" + ip + """'/></form>
        <iframe scrolling=no name=ipMapFrame width=275 height=430 style='margin:0px;padding:0px;overflow:hidden;border:none;'/>
        <script>document.getElementById('ipMap').submit();</script>
        """
    })


@viewsbp.route('/sampleUserInformation')
def sample_user_info():

    user = request.args.get('metaDataContext')

    return json.dumps({
        "key": "sampleUserInfo",
        "label": "Sample User Information",
        "value": "Sample information for a user called " + user
    })


@viewsbp.route('/sampleURLInformation')
def sample_url_info():

    return json.dumps({
        "key": "sampleURLInfo",
        "label": "Sample URL Information",
        "value": "Sample information for a URL"
    })


@viewsbp.route('/sampleToolbarButton')
def sample_toolbar_button():

    return json.dumps({
        "key": "sampleInfo",
        "label": "Sample Button",
        "value": "Sample Toolbar Button"
    })


@viewsbp.route('/sampleDashboardItem')
def sample_dashboard_item():

    return json.dumps({
        "id": "sampleItem",
        "title": "Sample Dashboard Item",
        "HTML": "<div>This item could contain <b><u>any HTML</u></b>!</div>"
    })


@viewsbp.route('/admin_screen')
def admin_screen():
    return render_template("admin_screen.html", title="Admin Me!")

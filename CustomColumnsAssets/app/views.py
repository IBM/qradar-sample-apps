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

from flask import Blueprint, escape
from qpylib import json_qpylib, qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# Custom columns require json in the format {'html':'<html to display in the column>'}
# In the endpoint below we create a div as the html and then use json_qpylib
# json_html helper function to generate the json above
@viewsbp.route('/get_custom_column/<asset_id>', methods=['GET'])
def get_column_html(asset_id):
    asset_type = get_asset_type(asset_id)
    # Follow OWASP rules for output encoding
    html = "<div id='asset_type'>{0}</div>".format(escape(asset_type))
    return json_qpylib.json_html(html)


# Uses QRadar rest api to look up the asset id and return the asset type from the api
# If it does not find the type it returns None
def get_asset_type(asset_id):
    params = {
        'filter': 'id={0}'.format(asset_id),
        'fields': 'interfaces(ip_addresses(type))'
    }
    asset_type = 'None'
    asset_api_response = qpylib.REST(rest_action='GET',
                                     request_url='/api/asset_model/assets',
                                     params=params)
    assets_json = asset_api_response.json()
    asset_json = assets_json[0]
    if 'interfaces' in asset_json:
        if 'ip_addresses' in asset_json['interfaces'][0]:
            if 'type' in asset_json['interfaces'][0]['ip_addresses'][0]:
                asset_type = asset_json['interfaces'][0]['ip_addresses'][0][
                    'type']
    return asset_type

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
@viewsbp.route('/get_custom_column/<offense_id>', methods=['GET'])
def get_column_html(offense_id):
    offense_severity = get_offense_severity(offense_id)
    # Follow OWASP rules for output encoding
    html = "<div id='offense_severity'>{0}</div>".format(
        escape(str(offense_severity)))
    return json_qpylib.json_html(html)


# Uses QRadar rest api to look up the offense id and return the severity from the api
# If it does not find the severity it returns 0
def get_offense_severity(offense_id):
    params = {'filter': 'id={0}'.format(offense_id), 'fields': 'severity'}
    offense_api_response = qpylib.REST(rest_action='GET',
                                       request_url='/api/siem/offenses',
                                       params=params)
    offenses_json = offense_api_response.json()
    offense_json = offenses_json[0]
    if 'severity' in offense_json:
        return offense_json['severity']
    return 0

# Copyright 2023 IBM Corporation
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

from flask import Blueprint, render_template
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    user_capabilities = get_user_capabilities()
    return render_template(
        'index.html',
        is_read_only_user=is_readonly_logsource_user(user_capabilities),
        has_capabilities=has_logsource_capabilities(user_capabilities))


def get_user_capabilities():
    response = qpylib.REST(
        'GET', 'api/config/access/user_roles?current_user_role=true')
    response_json = response.json()
    user_capabilities = response_json[0]
    return user_capabilities['capabilities']


def is_readonly_logsource_user(capabilities):
    for capability in capabilities:
        capability_name = capability['name']
        if capability_name in {
                'SYSTEM.LOGSOURCE', 'ADMIN', 'ADMINMANAGER', 'SAASADMIN'
        }:
            return False
    return True


def has_logsource_capabilities(capabilities):
    for capability in capabilities:
        capability_name = capability['name']
        if capability_name in {
                'SYSTEM.LOGSOURCE', 'ADMIN', 'ADMINMANAGER', 'SAASADMIN',
                'READONLYCONFIGURATION.LOGSOURCES.VIEW'
        }:
            return True
    return False

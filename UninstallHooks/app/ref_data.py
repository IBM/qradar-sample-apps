# Copyright 2022 IBM Corporation
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

from qpylib import qpylib

REFERENCE_DATA_MAP_NAME = "uninstall_hooks_app_ref_map"
REFERENCE_DATA_MAP_KEY = "arbitrary_key"
REFERENCE_DATA_INIT_VALUE = 100


def update_reference_data_value(value):
    qpylib.REST(
        'post', '/api/reference_data/maps/{0}?key={1}&value={2}'.format(
            REFERENCE_DATA_MAP_NAME, REFERENCE_DATA_MAP_KEY, value))


def get_reference_data_value():
    response = qpylib.REST(
        'get', '/api/reference_data/maps/{0}'.format(REFERENCE_DATA_MAP_NAME))
    if response.status_code == 404:
        create_reference_data_map_if_not_exists()
        return get_reference_data_value()
    resp_data = response.json()
    data = resp_data['data']
    reference = data[REFERENCE_DATA_MAP_KEY]
    return reference['value']


def delete_reference_data():
    response = qpylib.REST('delete',
                '/api/reference_data/maps/{0}'.format(REFERENCE_DATA_MAP_NAME))
    if response.status_code == 202:
        return {'result': 'success'}, 200
    return {'result': 'failed to delete reference data map'}, 500


def create_reference_data_key_if_not_exists(data):
    if REFERENCE_DATA_MAP_KEY not in data:
        # Key value doesn't exist, create new
        update_reference_data_value(REFERENCE_DATA_INIT_VALUE)


def create_reference_data_map_if_not_exists():
    response = qpylib.REST(
        'get', '/api/reference_data/maps/{0}'.format(REFERENCE_DATA_MAP_NAME))
    if response.status_code == 404:
        # Doesn't exist, create new
        response = qpylib.REST(
            'post',
            '/api/reference_data/maps?element_type=NUM&name={0}'.format(
                REFERENCE_DATA_MAP_NAME))
        resp_data = response.json()
        create_reference_data_key_if_not_exists(resp_data)
    else:
        resp_data = response.json()
        create_reference_data_key_if_not_exists(resp_data)

# Copyright 2020 IBM Corporation
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

qpylib.create_log()

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# A function that uses qpylib REST function to get a list of available Ariel databases.
# The authentication entry in manifest.json will allow qpylib REST functions to handle the authentication for the app.
def query_ariel_databases():
    try:
        response = qpylib.REST('get', '/api/ariel/databases')
        qpylib.log('response=' + str(response.json()))
        return response
    except Exception as ex:
        qpylib.log(
            'Error calling REST api GET /api/ariel/databases: ' + str(ex),
            'ERROR')
        raise


# An endpoint that gets a list of available Ariel databases by calling a python script which uses REST api call.
@viewsbp.route('/getArielDatabases')
def get_ariel_databases():
    response = query_ariel_databases()
    if response.status_code == 401:
        results = "A 'Deploy' is needed before this app can operate." \
                  "  Please navigate to 'Admin' tab and click 'Deploy Changes'."
    elif response.status_code == 200:
        results = response.json()
    else:
        qpylib.log(
            'get_ariel_databases() Unexpected response status code: ' +
            response.status_code, 'ERROR')
        results = "An unexpected error occurred see app logs for details."
    return render_template('oauth.html', results=results)

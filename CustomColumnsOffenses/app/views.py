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

__author__ = 'IBM'

from flask import Response, Blueprint
from qpylib import qpylib
from qpylib.offense_qpylib import get_offense_json_ld

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


@viewsbp.route('/custom_column_method/<offense_id>', methods=['GET'])
def get_offense(offense_id):
    try:
        offense_json = get_offense_json_ld(offense_id)
        return Response(response=offense_json,
                        status=200,
                        mimetype='application/json')
    except Exception as e:
        qpylib.log('Error calling get_offense_json_ld: ' + str(e), 'ERROR')
        raise

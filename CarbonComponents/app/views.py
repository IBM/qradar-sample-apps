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
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    return render_template('index.html')


@viewsbp.route('offenses')
def get_offenses():
    offense_range = request.args.get('range')
    response = qpylib.REST('get',
                           '/api/siem/offenses',
                           None,
                           headers={'Range': offense_range})
    return {'offenses': response.json()}


@viewsbp.route('offenses/<offense_id>')
def get_offense_by_id(offense_id):
    response = qpylib.REST('get', ('/api/siem/offenses/' + offense_id))
    return {'offense': response.json()}

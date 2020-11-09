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

__author__ = 'IBM'

from flask import Blueprint, render_template
from qpylib import qpylib
import json

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# build a Flask app route, this route will build a Json construct,
# of which there is a 'html' attribute to contain a html string
# This string is built from a Jinja2 template,
# and is based on using the q_url_for() method to build a url for resources, e.g. images
# which will adhere the proxying needs of passing through QRadar.
@viewsbp.route('/')
@viewsbp.route('/getExampleDashboardItem', methods=['GET'])
def getExampleDashboardItem():
    try:
        qpylib.log("getExampleDashboardItem>>>")
        return json.dumps({
            'id': 'ExampleDashBoardItem',
            'title': 'Example Dashboard',
            'HTML': render_template('dashboard.html')
        })
    except Exception as e:
        qpylib.log("Error " + str(e))
        raise

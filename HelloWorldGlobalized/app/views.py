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

from flask import Blueprint, render_template, request
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    # demonstrates how to request the accept-language header from qradar
    qpylib.log(request.headers.get('Accept-Language', ''))
    return render_template("index.html", title="QApp1 : Hello World !")

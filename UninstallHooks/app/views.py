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

from flask import Blueprint, render_template, request, redirect
from .ref_data import delete_reference_data, get_reference_data_value, update_reference_data_value

# pylint: disable=invalid-name
viewsbp = Blueprint('views', __name__, url_prefix='/')


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    return render_template('index.html', value=get_reference_data_value())


@viewsbp.route('/set_reference_data', methods=['POST'])
def set_reference_data():
    value = request.form['value']
    update_reference_data_value(value)
    return redirect('/', code=303)


@viewsbp.route('/uninstall_delete_reference_data', methods=['POST'])
def uninstall_delete_reference_data():
    delete_reference_data()
    return "OK!", 200

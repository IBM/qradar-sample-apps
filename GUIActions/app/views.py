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

from flask import Blueprint, request
from qpylib import qpylib

viewsbp = Blueprint('views', __name__, url_prefix='/')


@viewsbp.route('/listFunction')
def list_function():
    qpylib.log("ListFunction", "debug")

    # appContext will contain the id's from the selected table row/rows
    rows = request.args.get("appContext")
    qpylib.log("appContext=" + rows, "debug")

    # You can process the data and return any value here, that will be passed into javascript
    return rows

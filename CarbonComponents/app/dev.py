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

from flask import Blueprint, request
from qpylib import qpylib

# pylint: disable=invalid-name
devbp = Blueprint('devbp', __name__, url_prefix='/dev')

# This endpoint sets the app's minimum level for qpylib logging.
# Example call using curl:
#   curl -X POST -F "level=DEBUG" http://localhost:<port>/dev/log_level
@devbp.route('/log_level', methods=['POST'])
def log_level():
    level = request.form['level'].upper()
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    if level in levels:
        qpylib.set_log_level(level)
        return 'log level set to {0}'.format(level)

    return 'level value {0} missing or unsupported. Use one of {1}'.format(level, levels), 42

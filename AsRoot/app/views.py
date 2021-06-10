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

import pwd
from flask import Blueprint, render_template

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# Simple endpoint that displays the contents of sudoers
@viewsbp.route('/index')
def index():
    with open('/opt/app-root/store/sudoers', 'r') as file:
        text_formatted = " "
        for line in file:
            text_formatted += line + "</br>"
    file.close()
    return text_formatted
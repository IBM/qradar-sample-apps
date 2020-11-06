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

from flask import Blueprint, render_template, make_response, request
import random

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


@viewsbp.route('/index')
def index():
    return render_template('index.html')


@viewsbp.route('/cachecontrol.js')
def cachecontrol():

    nocache = request.args.get('nocache')

    if nocache is not None:
        nocache = int(nocache) * random.randint(0, 9)
    else:
        nocache = 0

    colour = '#{0:06X}'.format(nocache % (255 * 255 * 255))

    response = make_response(
        render_template('cachecontrol.js', nocache=nocache, colour=colour))
    response.headers['Content-Type'] = 'text/javascript'
    response.headers['Cache-Control'] = 'no-store'

    return response

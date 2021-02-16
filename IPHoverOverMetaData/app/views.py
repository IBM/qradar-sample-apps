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

import json
from flask import Blueprint, render_template, request, escape

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# Metadata providers are basically the pop-ups you see for example when hovering on certain elements in QRadar
# For example ip addresses in the log activity tab
# In order to create a metadata provider you need to have a json object with the following fields:
# key - This is a string used to uniquely identify the metadata provider
# label - This is the text that appears down the left hand side of the pop-up as the label to the metadata on the right.
# Then either of these two:
# html - This is html that will be displayed on the right hand side of the pop-up
# value - This is instead of html you can specify text to display in the right hand side of the pop-up
@viewsbp.route('/ip_metadata_provider')
def get_metadata():
    context = request.args.get('context')
    metadata_dict = {
        'key': 'exampleIPMetadataProvider',
        'label': 'Extra metadata:',
        # Be careful when rendering page content and refer to
        # OWASP rules for output encoding to learn how to prevent Cross Site Scripting (XSS)
        'html': render_template(escape('metadata_ip.html'), ip_address=context)
    }
    return json.dumps(metadata_dict)

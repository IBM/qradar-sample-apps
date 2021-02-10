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

from flask import Blueprint, render_template
from packaging import version as package_version
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')

# A list of features, paired with a list of known API versions that support the feature
FEATURES = [{
    'name': 'App multi-tenancy',
    'versions': ['13.0', '13.1', '14.0', '15.0', '15.1', '16.0', '17.0']
}, {
    'name': 'Proxy server API',
    'versions': ['13.0', '13.1', '14.0', '15.0', '15.1', '16.0', '17.0']
}, {
    'name': 'Certificate management API',
    'versions': ['16.0', '17.0']
}]


@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    # Retrieve the API versions, parsing into a JSON list
    response = qpylib.REST('get', '/api/help/versions')
    versions = response.json()
    # Iterate over the features and determine which ones are enabled
    enabled_features = []
    for feature in FEATURES:
        enabled_features.append({
            'name': feature['name'],
            'enabled': is_feature_enabled(feature, versions)
        })
    return render_template('index.html',
                           latest=get_latest_version(versions),
                           versions=versions,
                           features=enabled_features)


def get_latest_version(versions):
    latest = None
    for version in versions:
        # package_version.parse is from the packaging library, allows comparison of version strings
        if latest is None or package_version.parse(
                version['version']) > package_version.parse(latest):
            latest = version['version']
    return latest


def is_feature_enabled(feature, versions):
    # Determines if a feature is available by looping through the enabled versions and checking if there is an API
    # version enabled that supports the feature
    for feature_version in feature['versions']:
        for version in versions:
            if not version['removed'] and feature_version == version['version']:
                return True
    return False

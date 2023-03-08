# Copyright 2023 IBM Corporation
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

import os
import proxy_utils

from flask import Flask
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from qpylib import qpylib


# Flask application factory.
def create_app():
    # Create a Flask instance.
    qflask = Flask(__name__)

    # Initialize CSRF
    csrf = CSRFProtect()
    csrf.init_app(qflask)

    # Retrieve QRadar app id.
    qradar_app_id = qpylib.get_app_id()

    # Create unique session cookie name for this app.
    qflask.config['SESSION_COOKIE_NAME'] = f'session_{qradar_app_id}'

    # Set up flask session
    qflask.config["SESSION_PERMANENT"] = True
    qflask.config["SESSION_TYPE"] = "filesystem"
    Session(qflask)

    if 'QRADAR_FLASK_SECRET_KEY' in os.environ:
        qflask.config['SECRET_KEY'] = os.environ['QRADAR_FLASK_SECRET_KEY']
    elif 'QRADAR_APP_UUID' in os.environ:
        qflask.config['SECRET_KEY'] = os.environ['QRADAR_APP_UUID']

    # Hide server details in endpoint responses.
    # pylint: disable=unused-variable
    @qflask.after_request
    def obscure_server_header(resp):
        resp.headers['Server'] = f'QRadar App {qradar_app_id}'
        return resp

    # Register q_url_for function for use with Jinja2 templates.
    qflask.add_template_global(qpylib.q_url_for, 'q_url_for')

    # Initialize logging.
    qpylib.create_log()

    # To enable app health checking, the QRadar App Framework
    # requires every Flask app to define a /debug endpoint.
    # The endpoint function should contain a trivial implementation
    # that returns a simple confirmation response message.
    @qflask.route('/debug')
    def debug():
        return 'Pong!'

    # Import additional endpoints.
    # For more information see:
    #   https://flask.palletsprojects.com/en/1.1.x/tutorial/views
    from . import views
    qflask.register_blueprint(views.viewsbp)

    # Set proxy settings if present in file in http_proxy and https_proxy environment variables
    proxy_settings = proxy_utils.get_proxy_settings_from_json()
    proxy_utils.set_proxy_env_variables(proxy_settings)

    return qflask

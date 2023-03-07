# Licensed Materials - Property of IBM
# 5725I71-CC011829
# (C) Copyright IBM Corp. 2015, 2020. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

__author__ = 'IBM'

import os
import json

from flask import Flask
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from qpylib import qpylib
from . import proxy_utils


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
    from . import dev
    qflask.register_blueprint(dev.devbp)

    # Set proxy settings if present in file in http_proxy and https_proxy environment variables
    proxy_settings = proxy_utils.get_proxy_settings_from_json()
    proxy_utils.set_proxy_env_variables(proxy_settings)

    return qflask

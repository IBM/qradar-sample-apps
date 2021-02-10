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

__author__ = 'IBM'

import json
import secrets
from .db.database import db_exists, create_db, execute_schema_sql
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from qpylib import qpylib
from qpylib.encdec import Encryption, EncryptionError


# Flask application factory.
def create_app():
    # Create a Flask instance.
    qflask = Flask(__name__)

    csrf = CSRFProtect()
    csrf.init_app(qflask)

    # Retrieve QRadar app id.
    qradar_app_id = qpylib.get_app_id()

    # Create unique session cookie name for this app.
    qflask.config['SESSION_COOKIE_NAME'] = 'session_{0}'.format(qradar_app_id)

    secret_key = ""
    try:
        # Read in secret key
        secret_key_store = Encryption({'name': 'secret_key', 'user': 'shared'})
        secret_key = secret_key_store.decrypt()
    except EncryptionError:
        # If secret key file doesn't exist/fail to decrypt it,
        # generate a new random password for it and encrypt it
        secret_key = secrets.token_urlsafe(64)
        secret_key_store = Encryption({'name': 'secret_key', 'user': 'shared'})
        secret_key_store.encrypt(secret_key)

    qflask.config["SECRET_KEY"] = secret_key

    # Initialize database settings and flask configuration options via json file
    with open(qpylib.get_root_path(
            "container/conf/config.json")) as config_json_file:
        config_json = json.load(config_json_file)

    qflask.config.update(config_json)

    # Hide server details in endpoint responses.
    # pylint: disable=unused-variable
    @qflask.after_request
    def obscure_server_header(resp):
        resp.headers['Server'] = 'QRadar App {0}'.format(qradar_app_id)
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

    db_name = qflask.config["DB_NAME"]

    # create db if it doesnt exist and load schema
    if not db_exists(db_name):
        schema_file_path = qpylib.get_root_path("container/conf/db/schema.sql")
        create_db(db_name)
        execute_schema_sql(db_name, schema_file_path)

    return qflask

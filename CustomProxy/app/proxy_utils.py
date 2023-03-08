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

import json
import os

from flask import request
from qpylib import qpylib
from qpylib.encdec import Encryption, EncryptionError

PROXY_SETTINGS_JSON_FILE = qpylib.get_store_path('proxy_settings.json')

PROXY_PROTOCOL = 'proxy-protocol'
PROXY_SERVER = 'proxy-server'
PROXY_PORT = 'proxy-port'
PROXY_USERNAME = 'proxy-username'
PROXY_PASSWORD = 'proxy-password'

PROTOCOL = 'protocol'
SERVER = 'server'
PORT = 'port'
USERNAME = 'username'
PASSWORD = 'password'

# as this app does not require password encryption/decryption per user setting user to 'user'
USER = 'user'

HTTP_PROXY = 'http_proxy'
HTTPS_PROXY = 'https_proxy'


def build_proxy_url(proxy_settings):
    proxy_url = ''
    if PROTOCOL in proxy_settings:
        proxy_url += proxy_settings[PROTOCOL]
        proxy_url += '://'
    if USERNAME in proxy_settings:
        proxy_url += proxy_settings[USERNAME]
        if PASSWORD in proxy_settings:
            proxy_url += ':'
            proxy_url += proxy_settings[PASSWORD]
        proxy_url += '@'
    if SERVER in proxy_settings:
        proxy_url += proxy_settings[SERVER]
    if PORT in proxy_settings:
        proxy_url += ':'
        proxy_url += proxy_settings[PORT]
    return proxy_url


def get_proxy_settings_from_json():
    proxy_settings = {}
    if os.path.exists(PROXY_SETTINGS_JSON_FILE):
        try:
            with open(PROXY_SETTINGS_JSON_FILE, 'r') as json_file:
                proxy_settings = json.load(json_file)
                if PASSWORD in proxy_settings:
                    encryption = Encryption({
                        'name': PROXY_PASSWORD,
                        'user': USER
                    })
                    decrypted_proxy_password = encryption.decrypt()
                    proxy_settings[PASSWORD] = decrypted_proxy_password
        except OSError as os_error:
            qpylib.log(f'Unable to read proxy settings json file, {os_error}',
                       level='error')
        except EncryptionError as encryption_error:
            qpylib.log(
                f'Unable to decrypt proxy password in proxy settings json file, {encryption_error}',
                level='error')
    return proxy_settings


def write_proxy_settings_to_json(proxy_settings):
    try:
        encrypted_proxy_settings = proxy_settings.copy()
        if PASSWORD in encrypted_proxy_settings:
            encryption = Encryption({'name': PROXY_PASSWORD, 'user': USER})
            encrypted_proxy_password = encryption.encrypt(
                encrypted_proxy_settings[PASSWORD])
            encrypted_proxy_settings[PASSWORD] = encrypted_proxy_password
        with open(PROXY_SETTINGS_JSON_FILE, 'w') as json_file:
            json.dump(encrypted_proxy_settings, json_file)
            return True
    except OSError as os_error:
        qpylib.log(f'Unable to write proxy settings to json file, {os_error}',
                   level='error')
        return False
    except EncryptionError as encryption_error:
        qpylib.log(
            f'Unable to encrypt proxy password to add it to proxy settings json file, {encryption_error}',
            level='error')
        return False


def get_proxy_settings_from_form():
    proxy_settings = {}
    if request.form.get(PROXY_PROTOCOL):
        proxy_settings[PROTOCOL] = request.form.get(PROXY_PROTOCOL)
    if request.form.get(PROXY_SERVER):
        proxy_settings[SERVER] = request.form.get(PROXY_SERVER)
    if request.form.get(PROXY_PORT):
        proxy_settings[PORT] = request.form.get(PROXY_PORT)
    if request.form.get(PROXY_USERNAME):
        proxy_settings[USERNAME] = request.form.get(PROXY_USERNAME)
    if request.form.get(PROXY_PASSWORD):
        proxy_settings[PASSWORD] = request.form.get(PROXY_PASSWORD)
    return proxy_settings


def set_proxy_env_variables(proxy_settings):
    if proxy_settings:
        proxy_url = build_proxy_url(proxy_settings)
        if proxy_url:
            qpylib.log(f'proxy url is {proxy_url}', level='debug')
            os.environ[HTTP_PROXY] = proxy_url
            os.environ[HTTPS_PROXY] = proxy_url
        else:
            qpylib.log(
                'Unable to build proxy url, skipping setting environment variable',
                level='error')
    else:
        qpylib.log(
            'proxy settings was empty, skipping setting environment variables',
            level='debug')

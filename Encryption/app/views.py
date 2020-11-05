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

from flask import Blueprint, render_template, request
from qpylib.encdec import Encryption, EncryptionError

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# Endpoint serving the index file, with forms for encrypting/decrypting inputs.
@viewsbp.route('/index')
def index():
    return render_template('index.html')


# Endpoint that will encrypt and save the provided '?val' argument into the
# encdec encryption file with the key provided, which can be retrieved later
# with decryption.
@viewsbp.route('/encrypt/<key>')
def encrypt(key):
    # Get '?val=' query param
    value = request.args.get('val')
    # Encrypt the value with the key provided
    enc = Encryption({'name': key, 'user': 'user'})
    encrypted = enc.encrypt(value)
    return render_template('encrypt.html',
                           key=key,
                           value=value,
                           encrypted=encrypted)


# Endpoint that will load and decrypt a value from the encdec encryption file,
# referenced with the key provided.
@viewsbp.route('/decrypt/<key>')
def decrypt(key):
    # Set up encdec encryption
    enc = Encryption({'name': key, 'user': 'user'})
    try:
        # Attempt to decrypt the value
        decrypted = enc.decrypt()
        return render_template('decrypt.html',
                               key=key,
                               decrypted=decrypted,
                               key_found=True)
    except EncryptionError:
        # EncryptionError raised, handle the error with a template describing
        # that the decryption failed (for example if the key doesn't exist)
        return render_template('decrypt.html', key=key, key_found=False)

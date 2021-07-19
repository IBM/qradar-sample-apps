# Licensed Materials - Property of IBM
# 5725I71-CC011829
# (C) Copyright IBM Corp. 2015, 2020. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

from flask import Blueprint, render_template
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')

# # A simple "Hello" endpoint that demonstrates use of render_template
# # and qpylib logging.
# @viewsbp.route('/')
# def my_index():
#     return render_template('index.html', flask_token="Hello world")

@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    response = qpylib.REST('get', '/api/siem/offenses')
    offenses = response.json()
    return render_template('index.html', offenses=offenses)
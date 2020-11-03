# Copyright 2020 IBM Corporation All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

from flask import Blueprint, render_template
from qpylib import qpylib

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# Simple endpoint that grabs the instance's app ID and surfaces it by injecting
# it into HTML and returning it
@viewsbp.route('/index')
def hello():
    app_id = qpylib.get_app_id()
    return render_template('index.html', app_id=app_id)

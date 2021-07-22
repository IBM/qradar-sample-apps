# Licensed Materials - Property of IBM
# 5725I71-CC011829
# (C) Copyright IBM Corp. 2015, 2020. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

from flask import Blueprint, render_template

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')

@viewsbp.route('/')
@viewsbp.route('/index')
def index():
    return render_template('index.html')

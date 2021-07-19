# Licensed Materials - Property of IBM
# 5725I71-CC011829
# (C) Copyright IBM Corp. 2015, 2020. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

from flask import Blueprint, request
from qpylib import qpylib

# pylint: disable=invalid-name
devbp = Blueprint('devbp', __name__, url_prefix='/dev')

# This endpoint sets the app's minimum level for qpylib logging.
# Example call using curl:
#   curl -X POST -F "level=DEBUG" http://localhost:<port>/dev/log_level
@devbp.route('/log_level', methods=['POST'])
def log_level():
    level = request.form['level'].upper()
    levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

    if level in levels:
        qpylib.set_log_level(level)
        return 'log level set to {0}'.format(level)

    return 'level value {0} missing or unsupported. Use one of {1}'.format(level, levels), 42

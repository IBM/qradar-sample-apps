# Copyright 2020 IBM Corporation All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

import pwd
from flask import Blueprint, render_template

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# Simple endpoint that renders and serves 'users.html', displaying all UNIX
# users on the system
@viewsbp.route('/index')
def users():
    # Get all UNIX users and store their names in a list
    user_list = []
    for user in pwd.getpwall():
        user_list.append(user[0])
    # Render users.html using the retrieved user list
    return render_template('users.html', users=user_list)

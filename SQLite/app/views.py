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

from contextlib import closing
from flask import Blueprint, current_app, g, redirect, render_template, request, url_for
from .db.database import get_db_connection

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')


# get a db connection before request
def before_request():
    # Retrieve database settings from application configuration
    db_name = current_app.config["DB_NAME"]
    g.conn = get_db_connection(db_name)


# close db connection after request
def after_request(response):
    if hasattr(g, 'conn') and g.conn is not None:
        g.conn.close()
    return response


viewsbp.before_request(before_request)
viewsbp.after_request(after_request)


@viewsbp.route('/')
@viewsbp.route('/index')
def show_entries():
    cur = g.conn.cursor()
    with closing(cur):
        cur.execute('select title, text from entries order by id desc')
        entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@viewsbp.route('/add_entry', methods=['POST'])
def add_entry():
    cur = g.conn.cursor()
    with closing(cur):
        insert_query = 'insert into entries (title, text) values (?, ?)'
        cur.execute(insert_query,
                    (request.form['title'], request.form['text']))
        g.conn.commit()
    return redirect(url_for('viewsbp.show_entries'), code=303)

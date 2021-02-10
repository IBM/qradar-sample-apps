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

import os
import sqlite3
from contextlib import closing
from qpylib import qpylib

DB_STORAGE_PATH = qpylib.get_store_path('db')


# Check if the database name specified already exists, if so return True otherwise return False
def db_exists(db_name):
    return os.path.isfile(os.path.join(DB_STORAGE_PATH, db_name))


# Create the database specified in the parameters provided
def create_db(db_name):
    get_db_connection(db_name)


# Execute the specified sql file against the database in the parameters provided
def execute_schema_sql(db_name, schema_file_path):
    conn = get_db_connection(db_name)
    with conn:
        with open(schema_file_path, mode='r') as schema_file:
            cur = conn.cursor()
            with closing(cur):
                cur.executescript(schema_file.read())
                conn.commit()


# Get db connection to sqlite database using the parameter provided
def get_db_connection(db_name):
    db_path = os.path.join(DB_STORAGE_PATH, db_name)
    conn = sqlite3.connect(db_path)
    return conn

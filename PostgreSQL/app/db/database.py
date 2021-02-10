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

import psycopg2 as db_driver

from qpylib import qpylib

POSTGRES_DEFAULT_DATABASE_NAME = "postgres"


# Check if the database name specified already exists, if so return True otherwise return False
def db_exists(db_host, db_port, db_user, db_name):
    conn = get_db_connection(db_host, db_port, db_user,
                             POSTGRES_DEFAULT_DATABASE_NAME)
    with conn:
        # Check if a database already exists with the specified name if it does skip creation of the database
        cur = conn.cursor()
        with cur:
            query = 'SELECT EXISTS(SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower(%s));'
            cur.execute(query, (db_name, ))
            return cur.fetchone()[0]


# Create the database specified in the parameters provided
def create_db(db_host, db_port, db_user, db_name):
    conn = get_db_connection(db_host, db_port, db_user,
                             POSTGRES_DEFAULT_DATABASE_NAME)
    conn.autocommit = True
    with conn:
        cur = conn.cursor()
        with cur:
            # Database did not exist, create the database with the specified name
            cur.execute('CREATE DATABASE {0}'.format(db_name))


# Execute the specified sql file against the database in the parameters provided
def execute_schema_sql(db_host, db_port, db_user, db_name, schema_file_path):
    conn = get_db_connection(db_host, db_port, db_user, db_name)
    with conn:
        with open(schema_file_path, mode='r') as schema_file:
            cur = conn.cursor()
            with cur:
                cur.execute(schema_file.read())
                conn.commit()


# Get db connection to postgres database using the parameters provided
def get_db_connection(db_host, db_port, db_user, db_name):
    conn = db_driver.connect(host=db_host,
                             port=db_port,
                             user=db_user,
                             database=db_name)
    return conn

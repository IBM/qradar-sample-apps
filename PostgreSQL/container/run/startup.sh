#!/bin/bash
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

# Setting the locale explicitly for data consistency and Postgres
# It is good practice to explicitly choose a locale and stick with it
# In this example I am using the en_US locale but you can use your own locale of choice from the container.
# NOTE: en_US is also the app container default
as_root localedef -i en_US -f UTF-8 en_US.UTF-8
as_root 'echo "LANG=en_US.UTF-8" > /etc/locale.conf'

# Remove normal postgres folder if present we will be using /opt/app-root/store/db instead
# This database folder is in the mounted folder so data under this folder is persisted beyond the lifetime of the container
if [ -d /var/lib/pgsql ]; then
  as_root rm -rf /var/lib/pgsql
fi

if [ ! -d /var/run/postgresql ]; then
  as_root mkdir -p /var/run/postgresql
fi

as_root chown -R appuser:appuser /var/run/postgresql

# create database folder if not present
if [ ! -d "${APP_ROOT}"/store/db ]; then
  mkdir -p "${APP_ROOT}"/store/db
fi

# copy app postgres conf file to the database folder i.e. /opt/app-root/store/db
if [ -f "${APP_ROOT}"/store/db/postgresql.conf ]; then
  rm -f "${APP_ROOT}"/store/db/postgresql.conf
  cp "${APP_ROOT}"/container/run/postgresql.conf "${APP_ROOT}"/store/db/postgresql.conf
fi

as_root chmod 700 "${APP_ROOT}"/store/db
/usr/pgsql-10/bin/initdb -E UTF8 --locale=en_US.UTF-8 -D "${APP_ROOT}"/store/db
/usr/pgsql-10/bin/pg_ctl -D "${APP_ROOT}"/store/db -l logfile start

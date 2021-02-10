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

# This script is called on container shutdown if it exists.
# Note: any commands executed here should not take longer than 10 seconds otherwise they will be killed

Log "Performing cleanup, stopping database"
/usr/pgsql-10/bin/pg_ctl -D "${APP_ROOT}"/store/db stop
Log "Cleanup complete, database stopped"

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

#!/bin/bash
start=`date +%s`

printf "\nCleaning up existing containers/images...\n\n"
qapp clean -i

printf "\nBuilding React application...\n\n"
cd react-app && yarn build
cd ..

printf "\nStarting container...\n\n"
qapp run -d

end=`date +%s`
runtime=$((end-start))

printf "\nDone in $runtime seconds!\n"

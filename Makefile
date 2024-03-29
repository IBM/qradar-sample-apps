# Copyright 2020 IBM Corporation
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

lint:
	find . -name "*app"                             \
		-not -path "./NGINX/*"                      \
		-not -path "./AlternativeHTTPServer/*"      \
		-not -path "./NodeJS/*"                     \
		-not -path "./CarbonComponents/react-ui/*"  \
		| xargs pylint || exit 1

beautify:
	# Python beautify
	find . -name "*app" | xargs yapf -p -i -r
	# JSON beautify
	find . -name "*.json"               \
		-not -path "*/node_modules/*"   \
		-not -path "*/*/node_modules/*" \
		| xargs -I@ bash -c "cat @ | jq . > tmp.json && mv tmp.json @"

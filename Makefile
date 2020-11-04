# Copyright 2020 IBM Corporation All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0

lint:
	find . -name "*app" -not -path "./NGINX/*" | xargs pylint || exit 1

beautify:
	find . -name "*app"  -not -path "./NGINX/*" | xargs yapf --style pep8 -p -i -r
	find . -name "*.json" | xargs -I@ bash -c "cat @ | jq . > tmp.json && mv tmp.json @"

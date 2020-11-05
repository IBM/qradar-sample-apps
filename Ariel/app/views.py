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

from flask import Blueprint, render_template, request
from qpylib.ariel import ArielSearch, ArielError

import time
import json

# Response when a polling request times out
TIMEOUT_RESPONSE = {'Error': 'Query timed out'}

QUERY_ERROR = {"Error": "An error occurred while processing that query."}

POLLING_ATTEMPTS = 10

# pylint: disable=invalid-name
viewsbp = Blueprint('viewsbp', __name__, url_prefix='/')

# ArielSearch contains convenience methods to communicate with the QRadar API
ariel = ArielSearch()


@viewsbp.route('/index')
def index():
    """
    Index page, return HTML page with JavaScript embedded calling the
    different endpoints when submitted
    """

    return render_template('index.html')


@viewsbp.route('/search')
def search():
    """
    Creates a new search with the query provided, returns a search ID to allow further
    search interaction, such as retrieving results
    """

    # Get search ID
    query = request.args.get('query')

    # Try to get the search for a query,
    # if searching for the query failed then set response to QUERY_ERROR
    try:
        response = ariel.search(query)
    except ArielError:
        # If something goes wrong, return a query error and a HTTP 500 (Server Error) status code
        return json.dumps(QUERY_ERROR), 500

    # Return the response
    return json.dumps(response)


@viewsbp.route('/results')
def results():
    """
    Retrieves the results of a search
    """

    # Get search ID
    search_id = request.args.get('search_id')

    # Try to get the result of the query,
    # if the query failed set response to QUERY_ERROR
    try:
        response = ariel.results(search_id)
    except ArielError:
        # If something goes wrong, return a query error and a HTTP 500 (Server Error) status code
        return json.dumps(QUERY_ERROR), 500

    # Return the response
    return json.dumps(response)


@viewsbp.route('/poll')
def poll():
    """
    Repeatedly call the Ariel API to check if a search has finished processing
    if it has, retrieve and return the results
    Poll only as long as the timeout defined
    """

    # Get search ID
    search_id = request.args.get('search_id')

    # Number of times to poll the API before giving up
    attempts_remaining = POLLING_ATTEMPTS

    # Continually poll the API until the result can be returned
    while attempts_remaining > 0:

        try:
            # ariel.status() returns the tuple (response_status, search_id)
            # response[0] will either be 'WAIT' or 'COMPLETED' for a successful
            # request. An unsuccessful request will throw an ArielError which is
            # caught below.
            response = ariel.status(search_id)
            if response[0] == 'COMPLETED':
                break

            # Sleep for 1 second between queries
            # Keep pollings until 'attempts_remaining = 0'
            time.sleep(1)
            attempts_remaining -= 1
            continue

        except ArielError:
            # If something goes wrong, return a query error and a HTTP 500 (Server Error) status code
            return json.dumps(QUERY_ERROR), 500

    # The query ran out of attempts (Timeout)
    if attempts_remaining == 0:
        # If the request times out, return a timeout and a HTTP 408 (Timeout) status code
        return json.dumps(TIMEOUT_RESPONSE), 408

    # Try to get the result of the query,
    # if the query failed set response to QUERY_ERROR
    try:
        response = ariel.results(search_id)
    except ArielError:
        # If something goes wrong, return a query error and a HTTP 500 (Server Error) status code
        return json.dumps(QUERY_ERROR), 500

    # Return the response
    return json.dumps(response)

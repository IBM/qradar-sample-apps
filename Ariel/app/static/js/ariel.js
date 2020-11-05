/*
Copyright 2020 IBM Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

const QRadar = window.qappfw.QRadar;
/**
 * HTTP GET request to Flask endpoints
 * @param {string} inputID - input to read for any parameter to attach
 * @param {string} endpoint - the Flask endpoint to send the request to
 */

function request(inputID, endpoint) {

  // Parameter is initially set as empty string
  var param = '';
  if (inputID) {
      // If there is an inputID provided
      // Extract the parameter from the input
      param = document.getElementById(inputID).value;
  }

  // Each search box has its own response box to show the output of each response
  let response_div = document.getElementById('response_' + inputID.split('_')[0]);
  response_div.style.display = 'block';
  // Insert loading text while waiting for the response
  response_div.children[1].innerText = 'Loading ...';

  // Use QRadar's fetch API to send requests, by using QRadar.fetch,
  // QRadar takes care of inserting the appropriate headers (such as CSRF) for you.
  QRadar.fetch(endpoint + param, { method: "get" })
  // QRadar.fetch returns a promise, so .then() is used to check the response was successful
  .then(function(response) { if (response.ok) return response; else return Promise.reject(JSON.stringify({"Error": "Something went wrong processing your search."}, null, 4))  })
  // If the request was successful use response.json() to retreive the body of the request as JSON
  .then(function(response) { return response.json() })
  // Update the response box with the output of the response
  .then(function(response) {
    response_div.children[1].style.color = '#000'
    response_div.children[1].innerText = JSON.stringify(response, null, 4)
  })
  // If something went wrong, Promise.reject() move execution to here.
  // The response box is updated except this time the text is red to show an error occurred.
  .catch(function(error) {
    response_div.children[1].style.color = 'red'
    response_div.children[1].innerText = error
  })

}

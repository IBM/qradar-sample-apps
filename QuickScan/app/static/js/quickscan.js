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

// Instantiate the global QRadar class
const QRadar = window.qappfw.QRadar

// The two buttons the user can click
let createProfileButton = document.getElementById("create_profile")
let createProfileAndRunButton = document.getElementById("create_profile_and_run")

// Helper methods to enable/disable the buttons in the UI while a request is taking place
function enableButton(button) {
    button.disabled = false
}
function disableButton(button) {
    button.disabled = true
}

/**
 * Creates and optionally runs a new scan profile
 * @param {bool} inputID - A boolean which determines whether to run the profile after creating it
 */
function createProfile(runProfile) {

  // Grab the value from the 'scan_profile' textbox
  let profileName = document.getElementById("scan_profile").value
  // Get the value from the 'ip_addresses' textbox
  let ips = document.getElementById("ip_addresses").value
  // Get a reference to the 'output' element
  let output = document.getElementById("output")
  // Take the comma separated list of IP addresses and store
  // them in an array called 'ips_array'
  let ips_array = []
  ips.split(",").forEach(function(value) {
    ips_array.push(value.trim())
  })

  // Insert waiting text while the requests are pending
  output.innerHTML = "Please wait ..."

  // Use the QRadar fetch API alongside Javascript promises to create
  // and optionally run a new scan profile.
  QRadar.fetch("/api/scanner/profiles/create", {
    method: "post",
    body: JSON.stringify({
      name: profileName,
      ips: ips_array,
    })
  })
  .then(function(response) {

    // Update the output status if the new profile was created successfully or failed with an error
    if (response.status == 200)
      output.innerHTML = "Created new profile successfully."
    else
      output.innerHTML = "Failed to create new profile."

      return response

  })
  // Exit the promise chain if there was an error creating the profile
  .then(function(response) { if (response.status != 200) return Promise.reject("Error creating profile"); else return response })
  // Exit the promise chain after successfully creating the profile if 'runProfile' is false
  .then(function(response) { if (runProfile) return response; else return Promise.reject("Don't run profile") })
  // If 'createProfileAndRun' is clicked, use fetch to call '/api/scanner/profiles'
  .then(function(response) {
    return QRadar.fetch("/api/scanner/profiles", {method: "get"})
  })
  // Convert to output of 'GET /api/scanner/profiles' to JSON
  .then(function(response) { return response.json() })
  // Iterate over the array that's returned and get the 'scanProfileId' of the profile
  // whose name matches the previously created profile
  .then(function(response) {

    for (let scan of response) {

      if (scan.scanProfileName == profileName)
        return scan.scanProfileId;

    }

  })
  // Use the 'scanProfileId' to start a scan using the chosen profile
  .then(function(profileId) { return QRadar.fetch("/api/scanner/profiles/start?scanProfileId="+profileId, {method: "post"}) })
  // Output the status of the scan request, re-enable the buttons again
  .then(function(response) {

    if (response.status == 200)
      output.innerHTML = "Started scan successfully."
    else
      output.innerHTML = "Scan failed to start."

    enableButton(createProfileButton)
    enableButton(createProfileAndRunButton)

  })
  .catch(function() {
    // Re-enable the buttons
    enableButton(createProfileButton)
    enableButton(createProfileAndRunButton)
  })

}

// Add 'click' events to the two buttons the user can click
// The 'click' events attach a function to a button press
createProfileButton.addEventListener("click", function() {
  disableButton(createProfileButton)
  disableButton(createProfileAndRunButton)
  createProfile(false);
})

createProfileAndRunButton.addEventListener("click", function() {
  disableButton(createProfileButton)
  disableButton(createProfileAndRunButton)
  createProfile(true);
})

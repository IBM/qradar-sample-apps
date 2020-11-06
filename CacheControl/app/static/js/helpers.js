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

function loadNewScript() {

  // Remove old script element
  let oldScript = document.getElementById("cachesrc");
  oldScript.remove();

  // Replace with a new script element
  // Replacing is required to load the new Javascript file
  let newScript = document.createElement("script");
  newScript.id = "cachesrc";
  newScript.src = "cachecontrol.js?nocache="+ new Date().getTime();
  document.getElementsByTagName("body")[0].appendChild(newScript);

}

function updateResponse() {

  let loadedFrom = document.getElementById("loadedfrom");
  let newScript = document.getElementById("cachesrc");
  let url = new URL(newScript.src);
  let queryString = url.searchParams.get("nocache");
  loadedFrom.innerHTML = "Loaded a new Javascript file and bypassed browser cache (check browser network tab): <strong>cachecontrol.js?nocache=" + queryString + "</strong>";

}

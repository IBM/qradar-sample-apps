/*
Copyright 2021 IBM Corporation

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

function renderJsonContent(jsonTagId, targetDivTagId)
{
    // Read JSON data from provided JSON data tag
    var jsonTagContent = $("#" + jsonTagId).html();
    // Parse JSON data
    var json = JSON.parse(jsonTagContent);
    // Render to output tag
    $("#" + targetDivTagId).text(renderOffense(json));
}

function renderOffense(json)
{
    /* Be careful when rendering page content and refer to
    OWASP rules for output encoding to learn how to prevent Cross Site Scripting (XSS) */
    return 'id is ' + json.data.id;
}

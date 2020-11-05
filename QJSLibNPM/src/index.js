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

import { QRadar } from "qjslib";

const loadField = document.getElementById("qjslib-load-status");
const currentUserField = document.getElementById("current-user");
const installedAppsList = document.getElementById("installed-apps");

QRadar.fetch("/api/gui_app_framework/applications")
    .then((response) => response.json())
    .then((apps) => {
        for (const app of apps) {
            const appItem = document.createElement('li');
            appItem.appendChild(document.createTextNode(app.manifest.name));
            installedAppsList.appendChild(appItem);
        }
    })
    .catch((error) => alert(error));

const currentUser = QRadar.getCurrentUser()
currentUserField.innerText = currentUser.username;

loadField.innerText = "QJSLib loaded successfully"

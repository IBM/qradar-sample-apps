/*Copyright 2023 IBM Corporation

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

let viewLogSourcesButton = document.getElementById("view_log_sources_button");
let editLogSourceButton = document.getElementById("edit_log_source_button");
let clearLogSourcesButton = document.getElementById("clear_log_sources_table");

function enableButton(button) {
  button.disabled = false;
}
function disableButton(button) {
  button.disabled = true;
}

function showLoadingDiv() {
  document.getElementById("loading_div").style.display = "block";
}

function hideLoadingDiv() {
  document.getElementById("loading_div").style.display = "none";
}

function buildTableRow(logsource) {
  let rowHTML = '<tr>';
  rowHTML += '<td><input type="checkbox" /></td>';
  rowHTML += '<td>' + logsource['id'] + '</td>';
  rowHTML += '<td>' + logsource['name'] + '</td>';
  rowHTML += '<td>' + logsource['type_id'] + '</td>';
  rowHTML += '</tr>';
  return rowHTML;
}

function buildHeaderRow() {
  let headerHTML = '<tr>';
  headerHTML += '<th/>';
  headerHTML += '<th>ID</th>';
  headerHTML += '<th>Name</th>';
  headerHTML += '<th>Type ID</th>';
  return headerHTML;
}

function buildTable(logsources) {
  let tableHTML = '<table id="logsource_table">';
  tableHTML += buildHeaderRow();
  for (const logsource of logsources) {
    tableHTML += buildTableRow(logsource);
  }
  tableHTML += '</table>';
  return tableHTML;
}

function clearTable() {
  let tableDiv = document.getElementById("log_source_table_div");
  tableDiv.innerHTML = "";
}

viewLogSourcesButton.addEventListener("click", function () {
  showLoadingDiv();
  QRadar.fetch("/api/config/event_sources/log_source_management/log_sources?fields=id%2C%20name%2C%20type_id", { method: "GET" })
    .then(function (response) { return response.json() })
    .then(function (logsources) {
      hideLoadingDiv();
      let tableDiv = document.getElementById("log_source_table_div");
      tableDiv.innerHTML = buildTable(logsources);
    })
    .catch(function (error) {
      hideLoadingDiv();
      alert(error)
    });
});

editLogSourceButton.addEventListener("click", function () {
  let ls_table = document.getElementById("logsource_table");
  let checkboxes = ls_table.getElementsByTagName("input");

  if (checkboxes.length == 0) {
    alert("Please select the log source(s) you wish to edit below");
    return;
  }

  let message = "Log source(s) seleced to edit:\n";
  let checked_count = 0;
  for (let i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      let row = checkboxes[i].parentNode.parentNode;
      message += row.cells[1].innerHTML;
      message += ", " + row.cells[2].innerHTML;
      message += ", " + row.cells[3].innerHTML;
      message += "\n";
      checked_count++;
    }
  }

  if (checked_count == 0) {
    alert("Please select the log source(s) you wish to edit below");
  } else {
    alert(message);
  }
});

clearLogSourcesButton.addEventListener("click", function () {
  clearTable();
});
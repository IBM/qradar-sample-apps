# ReadOnlyLogSources

**Note**: This sample app will only work with QRadar 7.5.0 UP7+. 

It demonstrates how an app can enable/disable buttons in the UI to view or edit log sources based on the new *read-only view log sources capability* added in QRadar 7.5.0 UP7.

The sample app provides three buttons:

1. A view button to display the log source id, name and type_id in an html table requested via the REST API
2. An edit button that simply displays the log source data selected via the checkboxes in the table
3. A clear button to clear the table.

If the user has a user role with only the read-only view log sources capability they will only have the view and clear buttons enabled.
If the user doesn't have a user role with either admin capabilities, the manage log source capability or the read-only view log sources capability they will get a message saying they don't have the required capabilities and no buttons will be displayed.
If they have all of the above capabilities in their user role they will have all three buttons enabled.

## Running this app

First QJSLib should be downloaded from the GitHub releases page, in this example we are using `v1.1.1`:

```bash
curl -LJ https://github.com/IBM/qjslib/releases/download/1.1.1/qjslib-1.1.1.tgz \
    | tar -xvzO package/lib/qappfw.min.js > ./app/static/qjslib/qappfw.min.js
```

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```
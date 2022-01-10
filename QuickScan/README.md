# QuickScan

This sample app demonstrates how an app can allow users to send requests to the QRadar QVM API to create scan profiles.
The app operates entirely in JavaScript, using the QJSLib JavaScript library to handle sending requests to the QRadar
API.

The sample provides a simple interface for creating scan profiles and running them, allowing a user to name scan
profiles and target different IP addresses.

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

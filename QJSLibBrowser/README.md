# QJSLibBrowser

This sample app shows how to use the QJSLib JavaScript library by importing it as a browser script.

The app has an index page that uses QJSLib to retrieve and display the following:

- The status of loading QJSLib.
- The currently logged in user.
- A list of currently installed apps, retrieved from the API.

## Importing QJSLib

First QJSLib should be downloaded from the GitHub releases page, in this example we are using `v1.1.1`:

```bash
curl -LJ https://github.com/IBM/qjslib/releases/download/1.1.1/qjslib-1.1.1.tgz \
    | tar -xvzO ./package/lib/qappfw.min.js > ./app/static/qjslib/qappfw.min.js
```

In this sample, QJSLib exists in `app/static/qjslib/qappfw.min.js`, and can be imported by adding a reference to it in
HTML:

```html
<script src="./static/qjslib/qappfw.min.js"></script>
```

QJSLib can then be loaded in and used with:

```javascript
const QRadar = window.qappfw.QRadar;
```

Then QJSLib functions can be called, for example:

```javascript
QRadar.getCurrentUser()
```

## Running this app

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

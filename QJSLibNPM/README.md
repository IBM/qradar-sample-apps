# QJSLibNPM

This sample app shows how to use the QJSLib JavaScript library by importing it as an NPM package and bundling it up
using webpack.

The app has an index page that uses QJSLib to retrieve and display the following:

- The status of loading QJSLib.
- The currently logged in user.
- A list of currently installed apps, retrieved from the API.

## Importing QJSLib

In this sample, QJSLib is added as an NPM package dependency, which can be done in an NPM project by running:

```
npm install qjslib
```

QJSLib can then be loaded in and used with:

```javascript
import { QRadar } from "qjslib";
```

Then QJSLib functions can be called, for example:

```javascript
QRadar.getCurrentUser()
```

## Building this app

Building this app requires these dependencies:

- NodeJS
- NPM

Run the following to transpile and bundle the app code in `src/`:

```
npm install && npm run build
```

This will output the compiled and bundled JS code to `app/static/main.js`

## Running this app

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

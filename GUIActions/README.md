# GUIActions

This sample app demonstrates how to use *GUI actions* across five different areas of the QRadar UI:

- The logs activity page
- The network activity page
- The offenses page
- The assets page
- The vulnerabilities page

On each of these pages this app adds in a number of GUI actions, such as right click menu options, toolbar buttons, and
context menus.

## Page scripts

The app extensively uses *page scripts* to inject JavaScript functionality into each page, exposing a JavaScript
function `my_toolbar_button_action` that can be accessed and used from a GUI action.

## Running this app

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

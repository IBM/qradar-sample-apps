# Ariel

This sample app shows how you can use the QPyLib Ariel features to interact with the QRadar Ariel database.

This app provides a simple interface, allowing:

- User to input an AQL search query to send to the QRadar Ariel database and in return get a search UUID.
- User to get the results of a search by providing a UUID.
- Polling until a search is complete by UUID.

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

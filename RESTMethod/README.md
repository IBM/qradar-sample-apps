# RESTMethod

This sample app demonstrates how to use an app *REST method* to populate a dashboard item in QRadar. The app is simple
and uses Flask and Jinja to render a HTML page with a dropdown list of QRadar Ariel database names, retrieved from the
QRadar API using QPyLib. This list of QRadar Ariel database names visible as a dashboard item.

## Running this app

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

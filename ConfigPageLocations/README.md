# ConfigPageLocations

This sample app shows the locations of config pages, using Flask to display a
config page to the user in different config page locations in QRadar.

## Running this app

You can run this app locally by executing in this directory:

```bash
qapp run
```

Or you can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

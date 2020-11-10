# EnvironmentVariables

This sample app demonstrates how environment variables can be injected into an app by defining them in the app
manifest.

The app will display the value of three environment variables that have been injected from the app manifest:

- `ONE`
- `TWO`
- `THREE`

These values are retrieved in the Python Flask backend of the app and rendered into a Jinja HTML template.

> Please note: Do NOT use environment variables for storing secrets, this is not secure.

## App manifest

The section `environment_variables` in the app manifest defines the three environment variables that are injected.

```json
"environment_variables": [
    {
        "name": "ONE",
        "value": "1"
    },
    {
        "name": "TWO",
        "value": "2"
    },
    {
        "name": "THREE",
        "value": "3"
    }
]
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

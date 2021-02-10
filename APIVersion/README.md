# APIVersion

This example demonstrates how an app can query the `/api/help/versions` endpoint to retrieve API version information,
and use that information to determine which features are available to the app.

## API version endpoint

The `/api/help/versions` endpoint reports which API versions are available on QRadar. The endpoint reports which API
versions exist, if they are deprecated, and if they have been removed. This information can be used to determine which
API features are available to the app, allowing the app to customise its behaviour based on this.

A typical response from the endpoint looks like this:

```json
[
  ...
  {
    "version": "15.1",
    "deprecated": false,
    "removed": false,
    "root_resource_ids": [...],
    "id": 28,
  },
  {
    "version": "16.0",
    "deprecated": false,
    "removed": false,
    "root_resource_ids": [...],
    "id": 29,
  },
  {
    "version": "17.0",
    "deprecated": false,
    "removed": false,
    "root_resource_ids": [...],
    "id": 30,
  }
]
```

The `/api/help/versions` endpoint is available in QRadar API versions `6.0` and above.

## Running this app

You can run this app locally using the
[QRadar App SDK v2](https://exchange.xforce.ibmcloud.com/hub/extension/517ff786d70b6dfa39dde485af6cbc8b), executing the
following commands in this directory:

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

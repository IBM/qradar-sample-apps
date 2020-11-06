# AlternativeHTTPServer

This sample app demonstrates how a QRadar app can replace Flask with a different HTTP server using a named service. In
this example it uses the built in Python HTTP server, but the concepts outlined here could be applied to other types
of HTTP servers.

## App manifest

This app's manifest includes two key elements for replacing Flask, first it disables Flask from starting:

```json
"load_flask": "false",
```

The manifest also defines a named service to run instead of Flask, specifying the command to run to start the named
service, the port to run it on, and other configuration:

```json
"services": [
    {
        "command": "python3 -m http.server 5000",
        "directory": "/opt/app-root/app/",
        "endpoints": [],
        "name": "pythonhttpserver",
        "path": "/",
        "port": 5000,
        "version": "1"
    }
]
```

## Debug endpoint and health checks

Since Flask is disabled there must be a named service running on port `5000` (the default port) in order to respond to
health checks - letting QRadar determine if the app is running.

QRadar app health checks work by sending a request to the app on the default port (`5000`) at the endpoint `/debug`,
the app must respond with code `200` (`OK`) to let QRadar know that the app is running and has not crashed. Any payload
included in the response should be minimal and will be disregarded by QRadar.

In this example the file `app/debug` is returned by requests to the `/debug` health check, with a minimal payload that
results in a `200 OK` response, letting QRadar know that the app is running.

## Running this app

You can run this app locally by executing in this directory:

```bash
qapp run
```

Or you can package this app and deploy it by executing in this directory:

```bash
qapp package -p as_root.zip
```

and

```bash
qapp deploy -p as_root.zip -q <qradar console ip> -u <qradar user>
```

# NodeJS

> WARNING: Please be aware that using a NodeJS webserver is not recommended in a QRadar app, and will slow down the
> validation process. Avoid using a NodeJS webserver if possible, consider using a Python Flask webserver instead.

This sample app demonstrates how you can use a simple NodeJS webserver using express in a QRadar app.

## Dependencies

The app requires a number of dependencies, both at the OS level for running NodeJS, and at the application level for
installing the express library.

### RPMs

The app requires the *NodeJS* and *NPM* RPMs (stored in `container/rpm`) to be installed at app build time, allowing
the app to use NodeJS to run the server.

You can run the following command to download the required RPM dependencies:

```bash
docker run                                                    \
    -v $(pwd)/container/rpm:/rpm                              \
    registry.access.redhat.com/ubi8/ubi                       \
    yum download nodejs npm --downloaddir=/rpm
```

### NPM

The app requires the *Express* JavaScript library to be installed so NodeJS can serve HTTP requests. This is managed
through NPM, a JavaScript package management tool. The `package.json` and `package-lock.json` together specify a list
of dependencies the app requires, and their versions. Using the NPM package manager the dependencies can be downloaded
to the `node_modules` directory. This must be done before the app is packaged and ran.

To pull down any required dependencies, execute the following command in the `app/` directory:

```bash
npm ci
```

## App manifest

This app's manifest includes two key elements for running the NodeJS server, first it disables Flask from starting:

```json
"load_flask": "false",
```

The manifest also defines a named service to run NodeJS, specifying the command to run to start the named service, the
port to run it on, and other configuration:

```json
"services": [
    {
        "command": "node /opt/app-root/app/server.js",
        "directory": "/opt/app-root/app",
        "endpoints": [
            {
            "name": "appindexpage",
            "path": "/index",
            "http_method": "GET"
            }
        ],
        "name": "nodeservice",
        "path": "/index",
        "port": 5000,
        "version": "1",
        "stdout_logfile": "/opt/app-root/store/log/node_out.log",
        "stderr_logfile": "/opt/app-root/store/log/node_err.log"
    }
]
```

This defines that the NodeJS service (`nodeservice`) will be started by running `node /opt/app-root/app/server.js`,
operating out of the `/opt/app-root/app` directory.

## Health check and debug endpoint

Since Flask is disabled there must be a named service running on port `5000` (the default port) in order to respond to
health checks - letting QRadar determine if the app is running.

QRadar app health checks work by sending a request to the app on the default port (5000) at the endpoint `/debug`, the
app must respond with code `200` (`OK`) to let QRadar know that the app is running and has not crashed. Any payload
included in the response should be minimal and will be disregarded by QRadar.

In this example the `server.js` defines the response to any requests to the `/debug` endpoint to be `Pong!`.

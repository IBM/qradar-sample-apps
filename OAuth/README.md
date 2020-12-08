# OAuth

This app shows how you can use the QRadar OAuth functionality to authorize a QRadar app, granting an app authorization
privileges with the use of an authorized service.

## authentication

The `authentication` flag in the `manifest.json` file defines the OAuth process for authorizing the app.

```json
"authentication": {
    "oauth2": {
        "authorisation_flow": "CLIENT_CREDENTIALS",
        "requested_capabilities": [
            "SEM"
        ]
    }
}
```

The process defined is to use the `CLIENT_CREDENTIALS` OAuth flow, requesting the `SEM` capability. If the app is then
authorized by a user, QRadar will generate an *authorized service* with the `SEM` capability that the app can use.

## Installation and authorization process

1. OAuth enabled app install is started.
2. QRadar determines that the app is requesting OAuth authorization, installation is paused until authorization.
3. A user authorizes the app. This can be done through the GUI App Framework API, the QRadar App SDK, or through the
extension management UI if installing an extension.
4. Once the app has been authorized, the install will continue.
5. The app container will be injected with an environment variable called `SEC_ADMIN_TOKEN`; an authorized service
token which can be used to authenticate and authorize requests to QRadar, this is done automatically by QPyLib.

## Authorized service

QRadar uses *authorized services* to allow tools and services to authenticate and authorize themselves with QRadar,
allowing them to run with their own set of capabilities and the ability to run without direct user control - apps can
run in the background. The OAuth process uses these authorized services to provide credentials for OAuth apps.

## Running this app

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

# Custom proxy

This sample app shows how an app can override default proxies set up in an app's docker container if they have auto update populated in QRadar. By default if a proxy is specified in auto update in QRadar it is passed via the `http_proxy` and `https_proxy` environment variables to the app's docker container.

In this app a user can set up a custom proxy and can test the proxy is being used successfully by
making a HTTP GET request to an external URL. This URL must be one that cannot be accessed by either the QRadar console or by any proxy specified under the auto update settings otherwise it will not test the proxy override.

## Startup

At app startup `__init__.py` checks if there are proxy settings saved under `/opt/app-root/store/proxy_settings.json`. If the file exists and it's populated with the proxy settings it sets the environment variables `http_proxy` and `https_proxy` with these values to be used globally for all requests made by the requests library.

## Dependencies

This sample app uses the `flask-wtf` and `Flask_Session` Python libraries - these libraries can be downloaded using pip from
[PyPi](https://pypi.org/). The Python pip dependencies should be stored in the `container/pip` directory in the app
workspace.

You can run the following command to download the required pip dependencies:

```bash
pip download                     \
    --only-binary=:all:          \
    --platform manylinux1_x86_64 \
    --dest container/pip         \
    --no-deps                    \
    Flask_Session==0.4.0 cachelib==0.6.0 Flask-WTF==0.14.3 WTForms==2.3.3
```

## Running this app

To run this sample app locally using the QRadar App SDK, you must use a `qenv.ini` file to inject environment variables
into the local app container.

The `QRADAR_APP_UUID` is an environment variable used by the encdec Encryption module.

The `qenv.ini` file looks something like this:

```ini
[app]
QRADAR_APP_UUID=e7b57727-75e0-42f0-9e28-c4100a8e456c
QRADAR_FLASK_SECRET_KEY=f3dcaacc-8548-411b-aa99-83c7a52f0392
```

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

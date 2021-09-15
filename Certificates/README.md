# Certificates

This sample app shows how an app can support user certificate upload at runtime.

In this app a user can upload a certificate to trust, and can test the certificate has been added successfully by
making a HTTP GET request to a provided URL.

If a user wants to have the certificate trusted by QRadar as a whole, they can use the Certificate Management App
which is accessed by a link such as the one in this sample app.

## Importing certificates

QRadar apps can add custom certificates by placing the certificate in the certificate directory inside the persistant
storage directory with the path `/opt/app-root/store/certs`. Once a certificate has been added to this directory it
can be imported and trusted by running the `/opt/app-root/bin/update_ca_bundle.sh` script (this script must be run
with root privileges).

The sample app works by providing an `upload_cert` endpoint that allows a certificate to be uploaded. The endpoint
saves the uploaded cert to the certificate directory and then runs the `update_ca-bundle.sh` script to import it.

## Startup

At app startup the `container/run/import_certs.sh` script is ran, which sets up a directory in the persisted store for
holding certificates if it does not yet exist before running the `/opt/app-root/bin/update_ca_bundle.sh` script in the
container to import any certificates that have already been uploaded to the app and exist in the
`/opt/app-root/store/certs` certificates directory.

## Dependencies

This sample app uses the `flask-wtf` Python library - this library can be downloaded using pip from
[PyPi](https://pypi.org/). The Python pip dependencies should be stored in the `container/pip` directory in the app
workspace.

You can run the following command to download the required pip dependencies:

```bash
pip download                     \
    --only-binary=:all:          \
    --platform manylinux1_x86_64 \
    --dest container/pip         \
    --no-deps                    \
    Flask-WTF==0.14.3 WTForms==2.3.3
```

## Running this app

To run this sample app locally using the QRadar App SDK, you must use a `qenv.ini` file to inject environment variables
into the local app container.

The `QRADAR_APP_UUID` is an environment variable used by the encdec Encryption module.

The `qenv.ini` file looks something like this:

```ini
[app]
QRADAR_APP_UUID=e7b57727-75e0-42f0-9e28-c4100a8e456c
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

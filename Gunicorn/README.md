# Gunicorn

This sample shows how you can replace Flask with Gunicorn, running using Supervisord configuration.

## Gunicorn pips

This sample requires Gunicorn to be downloaded as a dependency before it can be run or deployed.

To download Gunicorn you can use `pip download`, execute the following command in this directory:

```bash
pip download                \
    --only-binary=:all:     \
    --platform linux_x86_64 \
    --dest container/pip    \
    gunicorn==20.0.4
```

This downloads the Gunicorn `.whl` file for `v20.0.4` to the `container/pip` directory. Any Python modules in this
directory will be picked up by QRadar when the app is built and installed.

## Manifest

The app manifest defines a named service called `gunicorn` that runs on the default port (`5000`) - this named service
allows the `gunicorn` webserver to be accessed.

## Supervisor

The `container/conf/supervisord.d` folder holds Supervisord configuration.

The file `container/conf/supervisord.d/gunicorn.conf` defines how Supervisord should start Gunicorn and configuration
for how the program should run, for example where to output log files and if the program should autorestart.

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

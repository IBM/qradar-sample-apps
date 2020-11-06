# NGINX

This sample app shows how to replace Flask with NGINX using Supervisord configuration.

The app simply sets up an area in the QRadar UI that is populated by a simple HTML webpage.

## NGINX RPMs

To download the NGINX RPMs required for this sample app, execute the following command in this directory (make sure
you have Docker installed):

```bash
docker run                                                    \
    -v $(pwd)/container/rpm:/rpm                              \
    registry.access.redhat.com/ubi8/ubi                       \
    yum download --resolve nginx-1.14.1 --downloaddir=/rpm
```

This will download the required NGINX RPMs into the `container/rpm` directory. This directory also contains an
`ordering.txt` file detailing which RPMs to install.

This will also download a version of OpenSSL which is not needed, and can be removed by executing:

```bash
rm container/rpm/openssl*-1.*.rpm
```

Create a new `ordering.txt` file which details which RPMs to install by executing:

```bash
ls container/rpm/ | grep -v "ordering.txt" > container/rpm/ordering.txt
```

NGINX RPMs are found in `container/rpm`, alongside a `ordering.txt` detailing which RPMs to install.

## Supervisor configuration

The Supervisor configuration is in `container/conf/supervisord.d`, specifically
`container/conf/supervisord.d/nginx.conf` which defines how the NGINX process is run.

## NGINX configuration

NGINX itself is configured with the `container/conf/nginx/nginx.conf` configuration file.

## Build scripts

Build scripts to set up a temporary directory for NGINX are in `container/build`, with a `build.sh` file and an
`ordering.txt` which holds a reference to the build script.

## App content

App content served through NGINX is in `app/`, including a simple `index.html` file for populating the app area, and
a `debug` file to respond to QRadar `/debug` healthchecks.

## Manifest

The app manifest disables Flask, sets up an area in the QRadar UI, and specifies a named service to run on port `5000`
(the default port) to expose the NGINX server.

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

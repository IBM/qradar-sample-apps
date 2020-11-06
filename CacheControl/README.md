# CacheControl

This sample app shows how a sample app can control the browser's cache.

Browsers normally cache static assets such as Javascript and CSS files to improve performance. However if a file is
changed after an app upgrade, for example, the browser cache will use the old version of the file rather than the one
from the upgrade.

This sample app has a button which when clicked loads a new Javascript file changing the colour of the title on the
screen.

It fetches a new Javascript file each time, using a query parameter and a timestamp to bypass the browser's cache. For
example:

```
cachecontrol.js?nocache=1597076610305
```

A new Javascript file is generated dynamically, with a new text colour, each time a request is made, to show the user
the browser's cache wasn't used.

This app also shows how to modify the headers returned in the browsers response.

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

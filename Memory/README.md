# Memory

This sample shows how you can choose the memory requirements for an app. This is a simple hello world app that has
300mb of memory assigned to it.

## Manifest

In the manifest under `resources` the `memory` field defines how much memory the app has in mb.

```json
"resources": {
    "memory": 300
}
```

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

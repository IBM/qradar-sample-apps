# IPHoverOverMetaData

This sample app demonstrates an app that provides hover over metadata information when hovering over an IP address in
the QRadar UI. This sample specifically displays some simple HTML and renders an image inside the hover over metadata.

## App manifest

The manifest configures the IP hover over 'metadata provider', specifying that the hover over should appear for data
of type `ip` (IP address) and should be populated by calling the `getIPMetadata` REST method.

```json
"metadata_providers": [
    {
        "rest_method": "getIPMetadata",
        "metadata_type": "ip"
    }
]
```

The manifest also configures the `getIPMetadata` REST method that the metadata provider calls, specifying that the
call should be made to the `/ip_metadata_provider` endpoint in the app's backend with a HTTP GET request. The IP
address value is provided with the `context` query parameter.

```json
"rest_methods": [
    {
        "name": "getIPMetadata",
        "url": "/ip_metadata_provider",
        "method": "GET",
        "argument_names": [
            "context"
        ]
    }
],
```

## HTML

The HTML template uses the `q_url_for` utility function to resolve the URL of the `IBM_security_logo.png` image in the
`static/images` folder. This means that at runtime this template will be rendered and this utility function will be
replaced with the correct URL to address the image.

## Running this app

Since this app injects data into the QRadar UI, you must run it through QRadar instead of running it locally.

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

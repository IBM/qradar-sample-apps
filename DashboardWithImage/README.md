# DashboardWithImages

This sample app demonstrates an app that provides a dashboard item that includes an image fetched from the Flask
static directory.

## App manifest

The manifest defines a REST method to expose an app endpoint so it can be called from the dashboard item:

```json
"rest_methods": [
    {
        "name": "getExampleDashboardItem",
        "url": "/getExampleDashboardItem",
        "method": "GET",
        "argument_names": [],
        "required_capabilities": [
            "ADMIN"
        ]
    }
]
```

The manifest also defines a dashboard item which uses the defined REST method:

```json
"dashboard_items": [
    {
        "text": "Example Item",
        "description": "Another Example dashboard item that is going to show some html with an image",
        "rest_method": "getExampleDashboardItem",
        "required_capabilities": [
            "ADMIN"
        ]
    }
],
```

The result of this is a dashboard item that will use the `/getExampleDashboardItem` to render the dashboard HTML.

## HTML

The HTML template uses the `q_url_for` utility function to resolve the URL of the `IBM_security_logo.png` image in the
`static/images` folder. This means that at runtime this template will be rendered and this utility function will be
replaced with the correct URL to address the image.

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

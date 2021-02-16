# MultiComponents

This sample app demonstrates how a single QRadar app can have many UI components. This sample app has the following
UI components:

- An area (tab)
- A dashboard item
- A configuration page
- A right click GUI action
- A toolbar button GUI action
- A page script
- Hover over (metadata) providers

## Area

The area appears as a tab in the main QRadar UI called *MultiComponent App* - opening this tab shows a simple HTML
page.

The area is configured in the manifest:

```json
"areas": [
    {
        "id": "QMultiComponentApp",
        "text": "MultiComponent App",
        "description": "An example of creating many GUI components from one app.",
        "url": "index",
        "required_capabilities": []
    }
],
```

This area is set up to send a query to the `/index` endpoint of the Flask backend, defined in the `app/views.py` file.

## Dashboard item

The dashboard item is an item a user can add to their dashboards, on the 'Dashboard' tab in the QRadar UI a user can
click the 'Add Item', then select 'MultiComponent App' and 'MultiComponentApp Item' to add the dashboard item to the
user's dashboard. In this sample the dashboard item is a simple HTML page.

The area is configured in the manifest:

```json
"dashboard_items": [
    {
        "text": "MultiComponentApp Item",
        "description": "Another Sample dashboard item that is going to show some HTML",
        "rest_method": "sampleDashboardItem",
        "required_capabilities": []
    }
],
```

This is paired with further configuration of the `sampleDashboardItem` REST method to allow the app's backend to serve
the dashboard content:

```json
"rest_methods": [
    {
        "name": "sampleDashboardItem",
        "url": "/sampleDashboardItem",
        "method": "GET",
        "argument_names": [],
        "required_capabilities": []
    },
    ...
]
```

The dashboard item and REST method definitions combined configure the dashboard item, naming it in the UI
`MultiComponentApp Item` and forwarding the query to `/sampleDashboardItem` in the app's backend. The backend is
defined in the `app/views.py`.

## Configuration page

The sample includes a configuration page, with a button to access it on the 'Admin' page with the label 'Open IBM.com'.
When the button is clicked a pop up appears and the configuration page is loaded in a new window, in this sample it
is a simple HTML page.

The configuration page is configured in the manifest:

```json
"configuration_pages": [
    {
        "text": "Open IBM.com",
        "description": "Loading IBM.com in a new window",
        "icon": null,
        "url": "admin_screen",
        "required_capabilities": [
            "ADMIN"
        ]
    }
],
```

This configuration page is configured to load the `/admin_screen` endpoint of the Flask backend, defined in the
`app/views.py` file.

## Right click GUI action

The sample includes a right click menu, which allows users to right click on an IP address in the QRadar UI and do
a custom action on the IP address. In this sample the right click action simply searches Google for the selected IP
address. You can try this out by right clicking on any IP address, for example in the 'Log Activity' table in the
QRadar UI, under 'More Options...' pick the 'Sample Right Click' action.

The right click menu is configured in the manifest:

```json
"gui_actions": [
    {
        "id": "sampleRightClick",
        "text": "Sample Right Click",
        "description": "Sample IP right click action that searches Google.",
        "icon": null,
        "javascript": "window.open('http://www.google.com?q='+context.innerText)",
        "groups": [
            "ipPopup"
        ],
        "required_capabilities": []
    },
    ...
]
```

This right click menu executes the JavaScript defined under `javascript` to open a new window at Google, accessing the
right clicked IP with `context.innerText`.

## Toolbar button GUI action

The sample includes a button in the toolbar, you can see this button on the 'Offenses' page, labelled as 'Sample
Toolbar Button'. This button both executes some JavaScript and calls a REST method.

The toolbar button is configured in the manifest:

```json
"gui_actions": [
    ...
    {
        "id": "sampleToolbarButton",
        "text": "Sample Toolbar Button",
        "description": "Sample toolbar button that calls a REST method, passing an offense ID along",
        "icon": null,
        "rest_method": "sampleToolbarMethod",
        "javascript": "alert('hello new button!')",
        "groups": [
            "OffenseListToolbar"
        ],
        "required_capabilities": []
    }
],
```

This toolbar is paired with a REST method:

```json
"rest_methods": [
    ...
    {
        "name": "sampleToolbarMethod",
        "url": "/sampleToolbarButton",
        "method": "GET",
        "argument_names": [
            "context"
        ],
        "required_capabilities": []
    },
    ...
],
```

The GUI action and REST method pair together mean that when the button is pressed both JavaScript will be executed and
an HTTP GET request will be sent to the `/sampleToolbarButton` endpoint of the Flask backend, defined in the
`app/views.py` file.

## Page script

The sample includes a page script, which allows a JavaScript file to be loaded in to a page of the QRadar, allowing
UI components to call the loaded JavaScript functions defined in the page script file.

The page script is configured in the manifest:

```json
"page_scripts": [
    {
        "app_name": "SEM",
        "page_id": "OffenseList",
        "scripts": [
            "static/js/sampleScriptInclude.js"
        ]
    }
],
```

This loads in the `app/static/js/sampleScriptInclude.js` JavaScript file from the Flask backend. The `app/static`
directory is configured to be served at the path `/static`.

## Hover over (metadata) providers

The sample includes three metadata providers, which are hover over menus - they provide additional metadata for hovered
over data.

The sample includes hover over information for three data types:

- Usernames
- IP addresses
- A URL field in the QRadar Event or Flow viewer

The `ariel:<field>` format allows a hover over to be added to any Ariel field, it matches agains a field with the
same name as the `<field>` selector after the `ariel:` group. In this example it is matching against the Ariel field
with the name `URL`.

These metadata providers are configured in the app manifest:

```json
"metadata_providers": [
    {
        "rest_method": "sampleIPInformation",
        "metadata_type": "ip"
    },
    {
        "rest_method": "sampleUserInformation",
        "metadata_type": "userName"
    },
    {
        "rest_method": "sampleURLInformation",
        "metadata_type": "ariel:URL"
    }
]
```

Each hover over directs to a `rest_method` which have also been configured in the app manifest:

```json
"rest_methods": [
    {
        "name": "sampleIPInformation",
        "url": "/sampleIpInformation",
        "method": "GET",
        "argument_names": [
            "metaDataContext"
        ],
        "required_capabilities": []
    },
    {
        "name": "sampleUserInformation",
        "url": "/sampleUserInformation",
        "method": "GET",
        "argument_names": [
            "metaDataContext"
        ],
        "required_capabilities": []
    },
    {
        "name": "sampleURLInformation",
        "url": "/sampleURLInformation",
        "method": "GET",
        "argument_names": [
            "metaDataContext"
        ],
        "required_capabilities": []
    }
],
```

Each endpoint is provided with the `metaDataContext` query parameter which includes the value in the field being
hovered over, allowing the backend to perform a lookup.

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

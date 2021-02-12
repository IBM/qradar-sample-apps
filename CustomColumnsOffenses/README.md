# CustomColumnOffenses

This sample app demonstrates an app that adds a custom column to the offenses page of QRadar. This extra column is
labelled as 'custom col custom javascript' and queries the app's Flask backend to populate the column. This app also
makes use of a page script to load in custom JavaScript in to the page which can then be used to render content in
the custom column.

## App manifest

The manifest defines the custom column, specifying the heading for the column as 'custom col custom javascript', where
the column should be added, in this case on the page with the `OffenseList` ID (the offenses page), and the HTTP
endpoint to send a GET request to with the column data to populate the column:

```json
"custom_columns": [
    {
        "label": "custom col custom javascript",
        "rest_endpoint": "custom_column_method",
        "page_id": "OffenseList"
    }
],
```

The manifest also defines a page script to load, specifying that it is found at the path `static/js/custom_offense.js`
and should be loaded on the page with the `OffenseList` ID (the offenses pages). This loads the JavaScript file
`custom_offense.js` that is served out of the Flask static directory, making the JavaScript available in the QRadar
UI on the offenses page.

```json
"page_scripts": [
    {
        "app_name": "SEM",
        "page_id": "OffenseList",
        "scripts": [
            "static/js/custom_offense.js"
        ]
    }
]
```

## Injecting data into the column with JavaScript

This app makes use of a special QRadar JavaScript function `renderJsonContent`; this function allows apps to use
JavaScript to render data in a custom column. The JavaScript function must have this signature:

```javascript
renderJsonContent(<JSON element ID>, <Custom column output element ID>)
```

This function recieves two IDs of HTML elements, the first being an HTML element that holds the data returned from
the custom column rest endpoint in JSON format, and the second being an HTML element that is inside the custom column
that is being rendered to. The process the JavaScript should use is this:

1. Read and parse the JSON from the JSON data element (first ID provided).
2. Write the output in the format desired to display to the custom column output element (second ID provided) in HTML.

You can see in this sample how this process works [in the `app/static/js/custom_offense.js`
file](app/static/js/custom_offense.js).

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

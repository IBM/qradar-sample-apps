# CustomColumnsAssets

This sample app demonstrates an app that adds a custom column to the assets page of QRadar. This extra column is
labelled as 'Asset Type' and queries the app's Flask backend to populate the column.

## App manifest

The manifest defines the custom column, specifying the heading for the column as 'Asset Type', where the column
should be added, in this case on the page with the `AssetList` ID (the assets page), and the HTTP endpoint to send
a GET request to with the column data to populate the column:

```json
"custom_columns": [
    {
        "label": "Asset Type",
        "rest_endpoint": "get_custom_column",
        "page_id": "AssetList"
    }
]
```

## Populating the column

The `app/views.py` file defines the app endpoints, with an endpoint for responding to QRadar with information to
populate the custom column with (`/get_custom_column/<asset_id>`). When an endpoint for a custom column is called by
QRadar some information is provided, with the identifier of the row provided in the request path to allow the endpoint
to perform a lookup, in this case the ID of the asset is provided.

When returning the HTML to inject into the column the endpoint must return it wrapped in JSON in the form:

```json
{
    "html": "<div>HTML to inject into the custom column</div>"
}
```

In this sample app QPyLib is used and the `json_html` utility function is used to wrap the HTML in this JSON format.

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

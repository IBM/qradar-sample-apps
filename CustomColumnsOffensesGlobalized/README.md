# CustomColumnsOffensesGlobalized

This sample app demonstrates an app that adds a custom column to the offenses page of QRadar. The heading of this
custom column is globalized into different languages and replaced at runtime by QRadar. The languages this app supports
are:

- US English (`en_US`)
- US English (`en`)
- Spanish (`es`)
- French (`fr`)

## Manifest globalization

The app uses *resource bundles* to globalize the values in the `manifest.json`, which are used by QRadar for
determining the naming of parts of the UI, for example the heading of a custom column would be decided in the app
manifest.

Anywhere in the manifest that a globalized value is needed a key is provided, for example the heading of a custom
column:

```json
"label": "customcolumn.label",
```

This means that to determine the heading of the custom column the key `customcolumn.label` will be looked up against
the appropriate language's resource bundle.

These keys are defined in resource bundles, you can see them in the `app/static/resources` directory. For example the
heading is set in the Spanish translation as:

```
customcolumn.label=Gravedad
```

The translation resource bundles are then referenced under `resource_bundles` in the app manifest:

```json
"resource_bundles": [
    {
        "locale": "en_US",
        "bundle": "resources/en_US.properties"
    },
    {
        "locale": "es",
        "bundle": "resources/es.properties"
    },
    {
        "locale": "fr",
        "bundle": "resources/fr.properties"
    },
    {
        "locale": "en",
        "bundle": "resources/en.properties"
    }
]
```

This allows QRadar to be able to look up these translations to determine what the manifest values should be and how
it should be displayed to users.

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

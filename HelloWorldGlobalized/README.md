# HelloWorldGlobalized

This sample app is a simple hello world app that has been globalized to several different languages. The languages
this app supports are:

- US English (`en`)
- Spanish (`es`)
- French (`fr`)
- Japanese (`ja`)

## Manifest globalization

The app uses *resource bundles* to globalize the values in the `manifest.json`, which are used by QRadar for
determining the naming of parts of the UI, for example the title of an *area* tab would be decided in the app manifest.

Anywhere in the manifest that a globalized value is needed a key is provided, for example the app name:

```json
"name": "hellog11n.app.name",
```

This means that to determine the app name it will look up the value using the key `hellog11n.app.name`.

These keys are defined in resource bundles, you can see them in the `app/static/resources` directory. For example the
app name is described in the Spanish translation with:

```
hellog11n.app.name=Hola Mundo
```

The translation resource bundles are then referenced under `resource_bundles` in the app manifest:

```json
"resource_bundles": [
    {
        "locale": "en_US",
        "bundle": "resources/hello_en_US.properties"
    },
    {
        "locale": "es",
        "bundle": "resources/hello_es.properties"
    },
    {
        "locale": "fr",
        "bundle": "resources/hello_fr.properties"
    },
    {
        "locale": "en",
        "bundle": "resources/hello_en.properties"
    },
    {
        "locale": "ja",
        "bundle": "resources/hello_ja.properties"
    }
]
```

This allows QRadar to be able to look up these translations to determine what the manifest values should be and how
it should be displayed to users.

## Application globalization

The application iteslf can be globalized with the use of a number of Python libraries that integrate with Flask and
provide language support that can be templated in using Jinja HTML templates.

### Dependencies

The sample app requires some Python libraries to manage globalization, they can be downloaded by running the following
command in this directory:

```bash
docker run                                    \
    -v $(pwd)/container/pip:/pip              \
    registry.access.redhat.com/ubi8/python-36 \
    pip download --no-deps --dest /pip pytz==2022.1 Babel==2.10.1 Flask-Babel==1.0.0 speaklater==1.3
```

This will download the required dependencies; these are referred to in the `ordering.txt` file in `container/pip` which
defines the order that the modules are installed in.

### Generating locale files

First install the required Python dependencies to your local machine by installing them from the `requirements.txt`
file:

```bash
pip install -r requirements.txt
```

Next the translation files should be compiled from `.po` to `.mo` binary files:

```bash
pybabel compile -d app/translations
```

These compiled `.mo` files are used at runtime to work with language headers and provide language support for the app.

## Running this app

> Please note: locale files must be compiled before the app will function properly.

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

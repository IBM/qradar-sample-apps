# SQLite

This sample app demonstrates how to use a SQLite database with a QRadar app. SQLite is included by default inside
QRadar's Red Hat Universal Base Image, so it does not need to be installed as an additional dependency.

## Secret key

This sample uses QPyLib's encryption module `encdec` to securely store a *secret key* for the app. This secret key is
used as part of the app's CSRF protection. Each app instance has its own secret key, which is generated at startup if
it does not already exist. If the secret key already exists it will be used instead of generating a new one.

In the app's Python startup code in `app/__init__.py` the secret handling is set up:

```python
    secret_key = ""
    try:
        # Read in secret key
        secret_key_store = Encryption({'name': 'secret_key', 'user': 'shared'})
        secret_key = secret_key_store.decrypt()
    except EncryptionError:
        # If secret key file doesn't exist/fail to decrypt it,
        # generate a new random password for it and encrypt it
        secret_key = secrets.token_urlsafe(64)
        secret_key_store = Encryption({'name': 'secret_key', 'user': 'shared'})
        secret_key_store.encrypt(secret_key)

    qflask.config["SECRET_KEY"] = secret_key
```

This code uses the `secrets` module to generate a random secret with 16 characters as a secret key.

## Configuration

The app has some additional configuration in `container/conf/config.json`:

```json
{
  "DEBUG": false,
  "DB_NAME": "mystore"
}
```

This configuration simply tells Flask to not run in debug mode, and includes an additional `DB_NAME` variable that can
be retrieved at runtime to get the name of the SQLite database.

This configuration is loaded by the Python startup code in `app/__init__.py` and provided as global configuration in
Flask:

```python
    # Initialize database settings and flask configuration options via json file
    with open(qpylib.get_root_path(
            "container/conf/config.json")) as config_json_file:
        config_json = json.load(config_json_file)

    qflask.config.update(config_json)
```

## Schema

The app's database schema is defined in `container/conf/db/schema.sql` as a SQL script. The Python app startup code in
`app/__init__.py` will execute this SQL against a new SQLite database if the database does not already exist:

```python
    # create db if it doesnt exist and load schema
    if not db_exists(db_name):
        schema_file_path = qpylib.get_root_path("container/conf/db/schema.sql")
        create_db(db_name)
        execute_schema_sql(db_name, schema_file_path)
```

> Please note, if you are maintaining SQL that should work across app updates and schema changes, consider using a SQL
> version control system, such as [FlywayDB](https://flywaydb.org/) or
> [golang-migrate](https://github.com/golang-migrate/migrate).

## Startup

At container startup the `container/run/startup.sh` script is run, this script creates a new directory `store/db` to
hold the SQLite databse. Since it is in the `store` directory the database will be persisted between app restarts and
upgrades.

## CSRF

The app uses the `flask-wtf` Python library to provide CSRF protection, which is globally configured from the Python
startup `app/__init__.py` code:

```python
    # Create a Flask instance.
    qflask = Flask(__name__)

    csrf = CSRFProtect()
    csrf.init_app(qflask)
```

This ensures that appropriate endpoints are protected with CSRF, using a secret key to generate and validate CSRF
tokens.

## Dependencies

This sample app uses the `flask-wtf` Python library - this library can be downloaded using pip from
[PyPi](https://pypi.org/). The Python pip dependencies should be stored in the `container/pip` directory in the app
workspace.

You can run the following command to download the required pip dependencies:

```bash
pip download                     \
    --only-binary=:all:          \
    --platform manylinux1_x86_64 \
    --dest container/pip         \
    --no-deps                    \
    Flask-WTF==0.14.3 WTForms==2.3.3
```

## Running this app

To run this sample app locally using the QRadar App SDK, you must use a `qenv.ini` file to inject environment variables
into the local app container.

The `qenv.ini` file looks something like this:

```ini
[app]
QRADAR_APP_UUID=e3260a5b-8c47-4c07-8a5a-8fcc535f60dd
```

The `QRADAR_APP_UUID` is an environment variable used by the encdec Encryption module.

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

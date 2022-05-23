# PostgreSQL

This sample app demonstrates how to use a PostgreSQL database with a QRadar app. PostgreSQL is not bundled with
QRadar's Universal Base Image, so must be installed at build time.

> Consider using a more lightweight database than PostgreSQL in an app, for example using a SQLite database. A
> PostgreSQL database should only be used with careful consideration - for example if the database is just storing
> configuration settings then SQLite or flat files would be more appropriate.

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
  "DB_NAME": "mystore",
  "DB_PORT": 5432,
  "DB_USER": "appuser",
  "DB_HOST": "localhost"
}
```

This configuration simply tells Flask to not run in debug mode, and includes some information for setting up
PostgreSQL; the name of the database, the database user, the port the database runs on, and the host the database
is running on.

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
`app/__init__.py` will execute this SQL against a new PostgreSQL database if the database does not already exist:

```python
    # create db if it doesnt exist and load schema
    if not db_exists(db_host, db_port, db_user, db_name):
        schema_file_path = qpylib.get_root_path("container/conf/db/schema.sql")
        create_db(db_host, db_port, db_user, db_name)
        execute_schema_sql(db_host, db_port, db_user, db_name,
                           schema_file_path)
```

> Please note, if you are maintaining SQL that should work across app updates and schema changes, consider using a SQL
> version control system, such as [FlywayDB](https://flywaydb.org/) or
> [golang-migrate](https://github.com/golang-migrate/migrate).

## Startup

At container startup the `container/run/startup.sh` script is run, this script is responsible for preparing the
container to run PostgreSQL, setting up a directory in `store/db` to store the database data and configuration,
alongside cleaning up default PostgreSQL files and initializing the PostgreSQL database.

## Shutdown

At container shutdown the `container/clean/cleanup.sh` script is run, this script is responsible for gracefully
shutting down the PostgreSQL database when an app container is stopped.

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

This sample app has a number of dependencies that are installed at build time, providing the PostgreSQL database, a
Python PostgreSQL database adapter, and a Python library for handling CSRF.

### RPM

This app installs PostgreSQL at build time using some RPMs. RPMs can be sourced using yum from the Red Hat package
repositories. RPM files should be stored in the `container/rpm` directory in the app workspace - any RPMs in this
directory will be picked up at build time and installed into the app image.

You can run the following command to download the required rpm dependencies:

```bash
docker run                                                    \
    -v $(pwd)/container/rpm:/rpm                              \
    registry.access.redhat.com/ubi8/ubi                       \
    /bin/bash -c 'yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm && yum download -y postgresql10 postgresql10-libs postgresql10-contrib postgresql10-server --downloaddir=/rpm --resolve'
```

This will also download a version of OpenSSL which is not needed, and can be removed by executing:

```bash
rm container/rpm/openssl*-1.*.rpm
```

### Python

This app uses the `flask-wtf` and `psycopg2` Python libraries - these libraries can be downloaded using pip from
[PyPi](https://pypi.org/). The Python pip dependencies should be stored in the `container/pip` directory in the app
workspace.

You can run the following command to download the required pip dependencies:

```bash
docker run                                    \
    -v $(pwd)/container/pip:/pip              \
    registry.access.redhat.com/ubi8/python-36 \
    pip download --no-deps --dest /pip Flask-WTF==0.14.3 WTForms==2.3.3 psycopg2-binary==2.8.6
```

## Running this app

To run this sample app locally using the QRadar App SDK, you must use a `qenv.ini` file to inject environment variables
into the local app container.

The `QRADAR_APP_UUID` is an environment variable used by the encdec Encryption module.

The `qenv.ini` file looks something like this:

```ini
[app]
QRADAR_APP_UUID=60f9f209-f6aa-4d87-b869-c102dcf3752c
```

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

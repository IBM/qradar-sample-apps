# Uninstall Hooks

This app shows how you can use the QRadar uninstall hook functionality to do cleanup on app uninstall.

QRadar 7.5.0+ includes uninstall hooks. An uninstall hook is a feature that allows an app to call a REST method as
part of the app uninstall process.

The lifecycle of the app uninstall hook is the following:

1. A request is made to delete an app definition.
2. The request is received and the app is placed into the `DELETING` state.
3. The uninstall hooks are executed if the deletion was by the ConfigServices user, otherwise the uninstall hooks are
skipped.
4. The app definition deletion continues as normal.

The uninstall hooks can only be called by the ConfigServices user since they are only run when uninstalling an
extension.
The ConfigServices user is a QRadar backend user used by the Extensions Management framework.

This example creates some reference data at startup, and then deletes that reference data when the app is uninstalled.

## REST method

There is a REST method defined in the manifest. This is the endpoint that is called by the uninstall hook.

```json
"rest_methods": [
  {
    "name": "uninstall_delete_reference_data",
    "url": "/uninstall_delete_reference_data",
    "method": "POST"
  }
],
```

When the uninstall hook is triggered a `POST` HTTP request will be sent to the `/uninstall_delete_reference_data`
endpoint in the app.

**Note**: the uninstall hook endpoint specified under rest_methods in the manifest json must:

* Return a success HTTP response code between 200->299 (inclusive).
* Return a valid JSON response, can be anything, but must be valid JSON, e.g. {} would be fine.

## Uninstall Hooks

There is an uninstall hook defined in the manifest. This lets QRadar know which REST method to call on uninstall, and
also configures the uninstall hook to only run when the last instance is uninstalled (for example in a multi-instance
multi-tenanted environment).

```json
"uninstall_hooks": [
  {
    "description": "Delete app reference data",
    "rest_method": "uninstall_delete_reference_data",
    "last_instance_only": "true"
  }
],
```

## Authentication

An OAuth2 authentication flow is defined in the manifest. This is because the uninstall hook runs in the background
of the app and requires admin capabilities to be able to delete any reference data that was created. Without this
the uninstall hook would not have permission to delete the reference data while operating as the ConfigServices
user.

```json
"authentication": {
  "oauth2": {
    "authorisation_flow": "CLIENT_CREDENTIALS",
    "requested_capabilities": [
      "ADMIN"
    ]
  }
}
```

## Running this app

You can package this app and deploy it by executing in this directory:

```bash
qapp package -p app.zip
```

and

```bash
qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

You will have to authorize this app for it to move from `CREATING` to `RUNNING`.

Once the app has successfully installed an extension can be created.

Use SSH to log in to QRadar as the root user.

Run the content management export tool to generate an extension:

```bash
/opt/qradar/bin/contentManagement.pl -a export -c installed_application -i <app id from the install>
```

The content management tool will report that an extension zip has been generated. You can install this extension
through the Extensions Management user interface in QRadar.

Once the app is installed you should be able to access the 'Uninstall hook ref data' area in the QRadar UI to modify
the reference data. You can see the reference data by sending a GET request to the
`/api/reference_data/maps/uninstall_hooks_app_ref_map` API endpoint on QRadar.

Now if you uninstall the extension through the extension UI you will see this reference data is cleaned up on
uninstall.

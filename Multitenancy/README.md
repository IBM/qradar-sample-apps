# Multitenancy

This app shows how to designate an app as 'multitenancy safe' - meaning the app has been tested and is ready to be used
in a multi-tenanted environment; with each tenant having a dedicated app instance.

This app simply reports the instance ID of the app instance that is serving the app content, allowing you to verify
that the app is serving from a different app instance per tenant.

## multitenancy_safe

The `"multitenancy_safe": "true"` flag in the `manifest.json` file designates this app as tested and ready for use in
a multi-tenanted environment. This allows a QRadar administrator to provision a dedicated app instance per tenant.

## Testing how this app works

You can test this app by first setting up a QRadar environment with two tenants with dedicated security profiles and
two users, with permissions to see the application.

The application should then be installed, and the QRadar administrator should provision a dedicated app instance for
each tenant (based on security profile).

To package and deploy the app use the SDK and execute the following in this directory:

```bash
qapp package -p multitenancy.zip
```

and

```bash
qapp deploy -p multitenancy.zip -q <qradar console ip> -u <qradar user>
```

To provision a new multitenanted instance of the app:

1. Get the installed application definition ID, search for the app 'Multitenancy' in the JSON returned by this API
request:

```bash
curl -X GET                            \
    -u <qradar user>:<qradar password> \
    https://<qradar console>/api/gui_app_framework/application_definitions
```

2. Take note of the security profile IDs, these can be listed with this API request:

```bash
curl -X GET                            \
    -u <qradar user>:<qradar password> \
    https://<qradar console>/api/config/access/security_profiles
```

3. Provision a dedicated app instance for each tenant (based on security profile):

```bash
curl -X POST                           \
    -u <qradar user>:<qradar password> \
    https://<qradar console>/api/gui_app_framework/applications?application_definition_id=<app definition id>&security_profile_id=<security profile id>
```

Now that each tenant should have its own dedicated instance, log in as each tenant user and view the 'Multitenancy
Single Instance' area, it should report the instance ID of the app serving the content; this ID should be different for
each tenant.

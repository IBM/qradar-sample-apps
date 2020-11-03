# AsRoot

This sample app shows how to use the `as_root` feature as part of a QRadar app.

This app creates a new UNIX user 'testuser' at startup time. The new user has  a home directory created outside of
`/opt/app-root` at `/home/testuser`.

## as_root

The `as_root` feature allows app developers the ability to run commands as the root user.

This sample app uses `as_root` in `container/build/add_user.sh`.

### Limitations

The `as_root` option is only available at app start up, if it is used during normal runtime operation it will fail.

### Considerations

The `as_root` option should only be used when neccessary, and is subject to strict validation (on submission to
X-Force Exchange) - there should be a justified and neccessary reason for using it.

## Running this app

You can run this app locally by executing in this directory:

```bash
qapp run
```

Or you can package this app and deploy it by executing in this directory:

```bash
qapp package -p as_root.zip
```

and

```bash
qapp deploy -p as_root.zip -q <qradar console ip> -u <qradar user>
```

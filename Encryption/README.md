# Encryption

This sample app shows how to use the QPyLib encdec encryption/decryption library as part of a QRadar app.

The app has an index page that allows input of keys and values to encrypt and then retrieve using decryption.

## Running locally

To run this sample app locally using the QRadar App SDK, you must use a `qenv.ini` file to inject environment
variables into the local app container.

The `QRADAR_APP_UUID` is an environment variable used by the encdec module.

## Encrypting values

Encdec can be used to encrypt values, storing them in a file identified by the provided `user` value. This file stores
the encrypted values, allowing them to be retrieved later, referenced by a name.

The idea behind naming the file based on the `user` property is that an app could have different secrets for different
users who use the app.

The encryption is set up with:

```python
enc = Encryption({'name': 'mytoken', 'user': 'myuser'})
```

This sets up an instance of the `Encryption` class that is dedicated to handling a single secret, in this example the
secret `mytoken` for user `myuser`.

Then the value is encrypted and saved to the encryption file referenced by the name:

```python
value = "value to be encrypted"
encrypted = enc.encrypt(value)
```

The `encrypt` function then returns the encrypted value, while also saving to the encryption file.

## Decrypting values

Encdec can also decrypt previously encrypted values, retrieving from the file referenced by the `user` value that the
secret was previously saved to.

Decryption is set up the same way that encryption is set up, with:

```python
enc = Encryption({'name': 'mytoken', 'user': 'myuser'})
```

Then the value can be retrieved and decrypted if it exists:

```python
decrypted = enc.decrypt()
```

The `decrypt` function returns the decrypted value referenced by the `name` property. If no `name` is found referencing
an encrypted value, or there is an issue with the encryption configuration, an `EncryptionError` is raised.

## Encryption engines

The QPyLib encdec functionality supports decrypting secrets from older encryption engine versions, and encrypting
secrets at the latest engine version.

At time of writing there are four encdec encryption engines:

- `v1` - Unsupported old version, previously distributed as a separate module from qpylib.
- `v2` - AES/CFB encryption.
- `v3` - Modified version of `v2` engine AES/CFB encryption.
- `v4` - Fernet encryption.

If an app has secrets encrypted using `v2`, `v3` or `v4` the encdec module will support decrypting these, even if they
are not the latest version - it will automatically determine the encryption engine to use. Once a secret that was
originally encrypted using an older engine version is decrypted, encdec will automatically re-encrypt the secret and
override the old secret. This allows for the encdec module to be used in a backwards compatible way, and if new engine
versions are released, old secrets are automatically migrated to newer encryption engine versions.

The encdec module will automatically store any secrets with the latest designated encryption engine, and coupled with
the backwards compatibility decryption and re-encryption of old versions should result in smooth transitions to the
recommended encryption engine version; only requiring QPyLib to be updated.

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

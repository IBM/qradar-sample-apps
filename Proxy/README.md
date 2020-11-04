# Proxy

This sample app shows how to retrieve and use QRadar proxy values manually from supplied environment variables.

The app has an index page that displays the retrieved proxy values, and uses them to make an HTTP request to the IBM
X-Force Exchange to retrieve the download count of the QRadar Assistant Extension (available as an unauthenticated
endpoint).

> Please note that manually setting up the proxy for a Python app is not necessary, QRadar provides the `https_proxy`,
> `http_proxy`, and `no_proxy` environment variables which are automatically picked up by Python libraries such as
> requests and QPyLib.
>
> If using another language/framework, check for built in support of these variables - if it is not supported the
> manual proxy values can be used.

## Proxy values from environment variables

QRadar injects a number of environment variables into apps to expose proxy information, libraries such as Python
requests and QPyLib will automatically pick up and use the following variables:

- `https_proxy`
- `http_proxy`
- `no_proxy`

Also injected are replicated equivalents which are designed to be manually retrieved and used as proxy variables:

- `QRADAR_HTTPS_PROXY`
- `QRADAR_HTTP_PROXY`
- `QRADAR_NO_PROXY`

### Configuration with nva.conf

The setting `APP_PROXY_ENABLED` in the `nva.conf` file determines if the following are injected:

- `https_proxy`
- `http_proxy`
- `no_proxy`

If `APP_PROXY_ENABLED=true` or `APP_PROXY_ENABLED` is not explicitly set the variables are injected, if
`APP_PROXY_ENABLED=false` they are not injected.

The setting `APP_PROXY_ENV_VARIABLES_ENABLED` in the `nva.conf` file determines if the following are injected:

- `QRADAR_HTTPS_PROXY`
- `QRADAR_HTTP_PROXY`
- `QRADAR_NO_PROXY`

If `APP_PROXY_ENV_VARIABLES_ENABLED=true` or `APP_PROXY_ENV_VARIABLES_ENABLED` is not explicitly set the variables are
injected, if `APP_PROXY_ENV_VARIABLES_ENABLED=false` they are not injected.

## Testing this App

Testing this app requires QRadar to be configured with a proxy, which can be configured by going to
*Admin -> Auto Updates -> Change Settings -> Advanced* and filling in the proxy values.

The app can then be built and deployed using the QRadar App SDK:

```
qapp package -p proxy.zip && qapp deploy -p proxy.zip -q <QRadar Console> -u <QRadar user>
```

Once the app is running, a new area should be visible on the QRadar console called 'Proxy'.

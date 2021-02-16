# QRadar sample apps

This repository holds a number of QRadar sample apps, built using v2 of the QRadar App Framework. These apps are
based on the Red Hat Universal Base Image, not the old CentOS 6 app image.

## Using these samples

To use the samples it is recommended you have the
[QRadar App SDK v2](https://exchange.xforce.ibmcloud.com/hub/extension/517ff786d70b6dfa39dde485af6cbc8b) installed,
which allows you to bundle apps through its command line interface and deploy them to QRadar, or even run the apps
locally.

Some apps require dependencies to be pulled down (if so it is explained in the apps' README), to pull down the required
dependencies make sure you have the following installed:

- [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) - To download
required Python modules.
- [Docker](https://docs.docker.com/get-docker/) - To download required Red Hat RPMs.
- [QRadar App SDK v2](https://exchange.xforce.ibmcloud.com/hub/extension/517ff786d70b6dfa39dde485af6cbc8b) - To run
apps locally and to deploy to a QRadar system.

## Samples

- [Replace Flask with an Alternative HTTP Server](./AlternativeHTTPServer)
- [Determine available QRadar API versions and features](./APIVersion)
- [Use the QPyLib Ariel features](./Ariel)
- [Run a command as root during app startup](./AsRoot)
- [Allow user uploaded custom certificate](./Certificates)
- [Add an extra column to the offenses table on the offenses page and uses JS to render
content](./CustomColumnsOffenses)
- [Add an extra column to the assets table on the assets page](./CustomColumnsAssets)
- [Add an extra column globalized to the offenses table on the offenses page](./CustomColumnsOffensesGlobalized)
- [Control browser cache](./CacheControl)
- [Provide a dashboard item with an image](./DashboardWithImage)
- [Use QPyLib to encrypt values](./Encryption)
- [Inject environment variables from the app manifest](./EnvironmentVariables)
- [Use GUI Actions](./GUIActions)
- [Replace Flask with Gunicorn](./Gunicorn)
- [Simple 'hello world' app](./HelloWorld)
- [Globalized 'hello world' app](./HelloWorldGlobalized)
- [Add hover over information to IP address data](./IPHoverOverMetaData)
- [Designate how much memory an app needs](./Memory)
- [Use multiple UI components (Areas, Dashboards, Config Pages, GUI Actions, Page Scripts, Metadata Providers) in a
single app](./MultiComponents)
- [Support multi-tenancy](./Multitenancy)
- [Use NGINX rather than Flask](./NGINX)
- [Use NodeJS rather than Flask](./NodeJS)
- [Use QRadar OAuth to authenticate the app](./OAuth)
- [Use a PostgreSQL database](./PostgreSQL)
- [Retrieve proxy values](./Proxy)
- [Use QJSLib imported through the browser](./QJSLibBrowser)
- [Use QJSLib imported through NPM](./QJSLibNPM)
- [Allow user submitted QRadar Vulnerability Manager scans](./QuickScan)
- [Use a REST method to populate a Dashboard Item](./RESTMethod)
- [Use a SQLite database](./SQLite)

## Project details

- [CONTRIBUTING](CONTRIBUTING.md)
- [MAINTAINERS](MAINTAINERS.md)

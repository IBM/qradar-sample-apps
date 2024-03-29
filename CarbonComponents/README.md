# CarbonComponents

This sample is an example of how to create a QRadar app with a React front end that uses Carbon components.

## Running this app

### Running locally

In order to run this app locally, you must first provide the following variables in the `qenv.ini` file:
- `QRADAR_CONSOLE_FQDN` - this will likely be the hostname of your QRadar instance;
- `QRADAR_CONSOLE_IP` - the IP address for your QRadar console instance;
- `SEC_ADMIN_TOKEN` - a secure access token generated by your QRadar console instance.

You must also install all necessary dependencies for the React app: from inside the `react-ui` directory run the following:

```bash
yarn install
```

You can then run the following command in this directory to build and start the application:

```bash
. store/scripts/clean-and-run.sh
```

### Deploying to QRadar

To deploy the application, ensure that you have provided the necessary variables in the `qenv.ini` file, then run the following commands in this directory:

```bash
. store/scripts/package.sh
```
and

```bash
qapp deploy qapp deploy -p app.zip -q <qradar console ip> -u <qradar user>
```

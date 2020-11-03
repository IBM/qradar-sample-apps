# Contributing

To contribute code or documentation, please submit a [pull request](https://github.com/ibm/qradar-sample-apps/pulls).

## Proposing new samples

If you would like to implement a new sample, please [raise an issue](https://github.com/ibm/qradar-sample-apps/issues)
before sending a pull request so that the sample can be discussed.

## Fixing bugs

To fix a bug, please [raise an issue](https://github.ibm.com/ibm/qradar-sample-apps/issues) before sending a
pull request so that the bug can be tracked.

## Merge approval

Any change requires approval before it can be merged.
A list of maintainers can be found on the [MAINTAINERS](MAINTAINERS.md) page.

## Legal

Each source file must include a license header for the Apache Software License 2.0.
Using the SPDX format is the simplest approach. See existing source files for an example.

## Development

On your local machine you can lint and beautify in mostly the same way that Travis CI does.

There are two commands you can run to make sure your code meets the required standards:

- `make lint` - Runs a linter against the code.
- `make beautify` - Runs a set of code beautifiers and does in-place code beautification.

### Dependencies

The following dependencies are required when developing these sample apps:

- [Python 3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)
- [jq](https://stedolan.github.io/jq/)
- Make (installed on most systems by default, for [windows see
here](http://gnuwin32.sourceforge.net/packages/make.htm))

The Python dependencies required can be installed using:

```bash
pip install -r requirements.txt
```

### Code style

Pull requests will be accepted only if `make lint` produces no warnings or errors and `make beautify` results in
no code changes.

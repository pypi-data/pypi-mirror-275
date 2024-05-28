# Python: Asynchronous client for the Fumis WiRCU API

![Project Stage][project-stage-shield]
![Project Maintenance][maintenance-shield]
[![License][license-shield]](LICENSE.md)

[![Build Status][build-shield]][build]
[![Code Coverage][codecov-shield]][codecov]

Asynchronous Python client for the Fumis WiRCU API.

## About

This package allows you to control and monitor Fumis WiRCU devices programmatically.
It is mainly created to allow third-party programs to automate the behavior of a Fumis WiRCU device.

An excellent example of this might be Home Assistant, which allows you to write automations, to turn on your pallet stove on or off and set
a target temperature.

## Usage

```python
import asyncio

from fumis_wircu import Fumis


async def main(loop):
    """Show example on controlling your Fumis WiRCU device."""
    async with Fumis(mac="AABBCCDDEEFF", password="1234", loop=loop) as fumis:
        info = await fumis.update_info()
        print(info)

        await fumis.set_target_temperature(23.0)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
```

## Contributing

This is an active open-source project.
We are always open to people who want to use the code or contribute to it.

We've set up a separate document for our [contribution guidelines](CONTRIBUTING.md).

Thank you for being involved! :heart_eyes:

## Setting up development environment

In case you'd like to contribute, a `Makefile` has been included to ensure a quick start.

```bash
make venv
source ./venv/bin/activate
make dev
```

Now you can start developing, run `make` without arguments to get an overview of all make goals that are available (including description):

```
$ make
Asynchronous Python client for the Fumis WiRCU API.

Usage:
  make help                            Shows this message.
  make dev                             Set up a development environment.
  make lint                            Run all linters.
  make lint-black                      Run linting using black & blacken-docs.
  make lint-flake8                     Run linting using flake8 (pycodestyle/pydocstyle).
  make lint-pylint                     Run linting using PyLint.
  make lint-mypy                       Run linting using MyPy.
  make test                            Run tests quickly with the default Python.
  make coverage                        Check code coverage quickly with the default Python.
  make install                         Install the package to the active Python's site-packages.
  make clean                           Removes build, test, coverage and Python artifacts.
  make clean-all                       Removes all venv, build, test, coverage and Python artifacts.
  make clean-build                     Removes build artifacts.
  make clean-pyc                       Removes Python file artifacts.
  make clean-test                      Removes test and coverage artifacts.
  make clean-venv                      Removes Python virtual environment artifacts.
  make dist                            Builds source and wheel package.
  make release                         Release build on PyP
  make tox                             Run tests on every Python version with tox.
  make venv                            Create Python venv environment.
```

## Authors & contributors

The original setup of this repository is by [Franck Nijhof][frenck].

For a full list of all authors and contributors, check [the contributor's page][contributors].

[build-shield]: https://github.com/aaronmunsters/fumis_wircu/workflows/Continuous%20Integration/badge.svg
[build]: https://github.com/aaronmunsters/fumis_wircu/actions
[codecov-shield]: https://codecov.io/gh/aaronmunsters/fumis_wircu/branch/main/graph/badge.svg
[codecov]: https://codecov.io/gh/aaronmunsters/fumis_wircu
[contributors]: https://github.com/aaronmunsters/fumis_wircu/graphs/contributors
[frenck]: https://github.com/frenck
[license-shield]: https://img.shields.io/github/license/aaronmunsters/fumis_wircu.svg
[maintenance-shield]: https://img.shields.io/maintenance/yes/2024
[project-stage-shield]: https://img.shields.io/badge/project%20stage-experimental-yellow.svg
[semver]: http://semver.org/spec/v2.0.0.html

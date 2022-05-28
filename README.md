# pyznn

Python SDK for interacting with the Zenon network and ecosystem.

# Setting up on local

If you want to contribute to this repo and looking for directions, follow along.

## Pre-requisites

- Python 3.8.10 (preferred)

We suggest using [`pyenv`](https://github.com/pyenv/pyenv-virtualenv) to easily manage python versions. Some of the following commands use `pyenv`.
Use [pyenv-installer](https://github.com/pyenv/pyenv-installer) for easy installation. Then add pyenv-virtualenv plugin to it.

### Configure local development environment

- Install and activate python 3.8.10 in the root directory

  - `pyenv install 3.8.10`
  - `pyenv virtualenv 3.8.10 pyznn`
  - `pyenv local pyznn`

- Install dev requirements

- `pip install -e ".[dev]"`

- Install precommit hook

  - `pre-commit install`

You're all set to hack!

Before making changes, let's ensure tests run successfully on local.

### Running Tests

- Run all tests with coverage
  - `coverage run -m pytest -v`
- Show report in terminal
  - `coverage report -m`

---
sidebar_position: 5
---

# Contributing

If you want to contribute to this repo and looking for directions, follow along.

## Setting up local dev

### Pre-requisites

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

## Raising PR

- Please fork this repo and push changes to your own feature branch
- Ensure that tests are covered
- Update the documentation website (markdown)
- Open a PR for review by core-team

# Firefox Screenshots Load Tests

[![Build Status](https://travis-ci.org/mozilla-services/screenshots-loadtests.svg?branch=master)](https://travis-ci.org/mozilla-services/screenshots-loadtests)

Async [**Firefox Screenshots**](https://github.com/mozilla-services/screenshots) load tests using [**molotov**](https://github.com/loads/molotov).

## Requirements:

- [Python 3.5+](https://www.python.org/downloads/)

## Installation:

```sh
$ virtualenv venv -p python3
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

## Usage:

```sh
$ molotov -h

$ molotov -cvv --max-runs 1
```

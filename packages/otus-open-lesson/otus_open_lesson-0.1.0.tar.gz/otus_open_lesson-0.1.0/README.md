# otus-open-lesson

DRF Testing package

## Menu

- [Mission](#mission)
- [Open Source Project](#open-source-project)
- [Features](#features)
- [Requirements](#requirements)
- [Development Status](#development-status)
- [Install](#install)
- [Quickstart](#quickstart)
- [Contributing](#contributing)

## Mission

To demonstrate how to create python-django package with test cases

## Features

- Demo project
- Demo package
- Workflows

## Requirements

- django, djangorestframework, markdown, django-filter

## Development Status

- Package already available on [PyPi](https://pypi.org/project/otus-open-lesson/)

## Install

### with pip

```commandline
pip install otus-open-lesson
```

## Quickstart

Add package to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...,
    'otus_open_lesson',
]
```

Run tests

```commandline
python manage.py test
```

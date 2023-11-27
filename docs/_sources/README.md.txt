**Platform Supported**

![Generic badge](https://img.shields.io/badge/Platform-Linux|MacOS|Windows-1f425f.svg)

**Deployments**

[![pages-build-deployment](https://github.com/thevickypedia/volume-control/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/thevickypedia/volume-control/actions/workflows/pages/pages-build-deployment)
[![pypi-publish](https://github.com/thevickypedia/volume-control/actions/workflows/python-publish.yml/badge.svg)](https://github.com/thevickypedia/volume-control/actions/workflows/python-publish.yml)

# Volume Control
Light weight OS-agnostic volume controller for python

### Installation
```shell
python -m pip install volume-control
```

### Usage
```python
import pyvolume

pyvolume.custom(percent=30)
```

### Optional arguments
- **debug:** Display logs in the form of `info`, `warnings` and `errors` messages.
- **logger:** Bring your own [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger) for custom logging.

## Coding Standards
Docstring format: [`Google`](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) <br>
Styling conventions: [`PEP 8`](https://www.python.org/dev/peps/pep-0008/) <br>
Clean code with pre-commit hooks: [`flake8`](https://flake8.pycqa.org/en/latest/) and 
[`isort`](https://pycqa.github.io/isort/)

## [Release Notes](https://github.com/thevickypedia/volume-control/blob/main/release_notes.rst)
**Requirement**
```shell
python -m pip install gitverse
```

**Usage**
```shell
gitverse-release reverse -f release_notes.rst -t 'Release Notes'
```

## Linting
`PreCommit` will ensure linting, and the doc creation are run on every commit.

**Requirement**
```shell
pip install sphinx==5.1.1 pre-commit recommonmark
```

**Usage**
```shell
pre-commit run --all-files
```

## Pypi Package
[![pypi-module](https://img.shields.io/badge/Software%20Repository-pypi-1f425f.svg)](https://packaging.python.org/tutorials/packaging-projects/)

[https://pypi.org/project/volume-control/](https://pypi.org/project/volume-control/)

## Runbook
[![made-with-sphinx-doc](https://img.shields.io/badge/Code%20Docs-Sphinx-1f425f.svg)](https://www.sphinx-doc.org/en/master/man/sphinx-autogen.html)

[https://thevickypedia.github.io/volume-control/](https://thevickypedia.github.io/volume-control/)

## License & copyright

&copy; Vignesh Rao

Licensed under the [MIT License](https://github.com/thevickypedia/volume-control/blob/main/LICENSE)

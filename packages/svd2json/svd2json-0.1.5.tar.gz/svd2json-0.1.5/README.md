<!--
SPDX-FileCopyrightText: 2024 Ledger SAS
SPDX-License-Identifier: Apache-2.0
-->
# Python svd2json package

This package converts a [CMSIS SVD (System View Description)](https://arm-software.github.io/CMSIS_5/SVD/html/index.html) file into a more friendly JSon format than raw XML to JSon conversion.
The aim of this package is to ease code generation from SVD file. We state that JSon format is the
best suitable for this purpose. For instance, it can be used as-is in Jinja2 template processing.

## JSon format

The resulting JSon `root` node is the `device` node in SVD.
XML values are converted to equivalent JSon ones.

> **_NOTE:_** Some SVD files might be inconsistent in peripherals and/or registers naming convention across devices or in a single SVD file. E.g. only few registers are prefixed by peripheral name but no others, you can optionally trim this prefix in order to keep code generation as simple as possible and reusable among a wide range of devices/mcu. !!ADD REF!!

An Additional `interrupts` is added in the resulting JSon which collects all interrupts declared across all peripherals. This can ease, for instance, `VTOR` table generation, one only has to walk through this array.

## Script
This package exports the following script:
### svd2json
```console
$ svd2json --help
usage: svd2json [-h] -s SVD output

convert svd file to json

positional arguments:
  output             output filename

options:
  -h, --help         show this help message and exit
  -s SVD, --svd SVD  SVD file to convert
```

## How to ...
This package follows PEP517/518/621 for its build system using a single `pyproject.toml` file and `setuptools` with dynamic versioning as build-backend. Unit testing, linting etc. are done with `tox`.
The minimal python version is Python 3.10.

#### Build
One can use any python build front-end. E.g. with [PyPA `build` front-end](https://github.com/pypa/build) :

```console
python -m build
```

#### Lint
This package is linted by [`black`](https://black.readthedocs.io/en/stable/) and [`flake8`](https://flake8.pycqa.org/en/latest/). In case of conflict between those two linter, we choose to follow `black` rules by default as it is closer to `PEP8` than `flake8`.

```console
tox -e lint
```

#### Type check
Type checking is done with [mypy](https://mypy-lang.org/) with a python 3.10+ syntax.

```console
tox -e type
```

#### License check
Package license(s) can be checked using [reuse](https://reuse.software/).

```
tox -e licenses
```

#### Doc
Documentation is generated using [`Sphinx`](https://www.sphinx-doc.org/en/master/index.html) and using
the [numpy style](https://numpydoc.readthedocs.io/en/latest/format.html) for pythondoc with [napoleon extension](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html).

```console
tox -e docs
```

#### Unit tests
Package Unit tests are based on `pytest` with coverage support.

```console
tox -e unittests
tox -e htmlcov
```

## License
Licensed under Apache-2.0

> see [LICENSE](LICENSES/Apache-2.0.txt) file

# feefifofum

<div align='center'>

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Tests](https://github.com/rushwerks/feefifofum/actions/workflows/tests.yaml/badge.svg)](https://github.com/rushwerks/feefifofum/actions/workflows/tests.yaml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)

</div>

Fee-fi-fo-fum is a simple and lightweight (fe)ature (fi)le (fo)rmatter written in Python.

It allows you to easily format `.feature` files (used in Behavior Driven Development) according to predefined rules.

## Formatting
The formatter follows a list of pre-defined rules outlined below.

### New lines
* Two new lines between scenarios
* One new line between all steps

### Indentation
* Two spaces for indentation
* Indent one level for each feature file keyword, resulting in:
    * `Feature`: Zero spaces
    * `Scenario`: Two spaces
    * `Given`/`When`/`Then`/`And`: Four spaces
    * Tables/step text: Six spaces

## Installation
Install the feefifofum directly from GitHub by running the following command:
```shell
pip install git+https://github.com/rushwerks/feefifofum.git@v0.1.1
```

## Usage
Format any number of feature files or directories containing feature files, by providing a list of path arguments. If directory paths are provided, then feature files will be searched recursively downward from these paths.

```shell
feefifofum <file>
feefifofum <file1> <file2> <file3>
feefifofum <directory1> <directory2>
```

## Pre-commit
`feefifofum` is also available as a pre-commit hook. It can be configured as follows:
```yaml
  - repo: https://github.com/rushwerks/feefifofum/
    rev: v0.1.1
    hooks:
      - id: feefifofum
```

## Table format
Feature files should have a single table per step (`Given`/`When`/`Then`/`And`). This assumption is used to identify tables, by tracking changes of pipe (`|`) characters on each line.

Each row of a table must also:
* Start with pipe character
* End with a pipe character
* Have a consistent number of pipe characters
* Only use a single pipe character for each cell's boundary

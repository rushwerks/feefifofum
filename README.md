# feefifofum

<div align='center'>

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Tests](https://github.com/rushwerks/feefifofum/actions/workflows/tests.yaml/badge.svg)](https://github.com/rushwerks/feefifofum/actions/workflows/tests.yaml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)

</div>

Fee-fi-fo-fum (`feefifofum`) is a simple and lightweight (fe)ature (fi)le (fo)rmatter written in Python.

A `.feature` file is a plain-text file written in Gherkin syntax, and is used in Behavior Driven Development (BDD) to define test scenarios for software.

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
    * Tables/step comments: Six spaces

## Installation
Install  `feefifofum` directly from GitHub by running the following command:
```shell
pip install git+https://github.com/rushwerks/feefifofum.git@v0.2.0
```

## Usage
`feefifofum` can run directly on feature files or directories containing feature files.
If directory paths are provided, then feature files in all subdirectories will also be formatted.

```shell
feefifofum <file>                     # Format a single file
feefifofum <file1> <file2> <file3>    # Format multiple files
feefifofum .                          # Format all feature files in current directory and subdirectories
feefifofum <directory>                # Format all feature files in specified directory and any subdirectories
feefifofum <directory1> <directory2>  # Format all feature files in multiple directories (and any of their subdirectories)
```

### Output
In its default setting, `feefifofum` will only log the total number of files formatted to the console.
The `--verbose` or `-v` flag can be passed to log information on which files have been formatted and overall progress.
```shell
feefifofum <file1> <file2> <file3> --verbose
```

## Pre-commit
`feefifofum` is also available as a pre-commit hook. It can be configured as follows:
```yaml
  - repo: https://github.com/rushwerks/feefifofum/
    rev: v0.2.0
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

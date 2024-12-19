# feefifofum

<div align='center'>

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Tests](https://github.com/rushwerks/feefifofum/actions/workflows/tests.yaml/badge.svg)](https://github.com/rushwerks/feefifofum/actions/workflows/tests.yaml)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v0.json)](https://github.com/charliermarsh/ruff)

</div>

Fee-fi-fo-fum (`feefifofum`) is a simple and lightweight (fe)ature (fi)le (fo)rmatter written in Python.

A `.feature` file is a plain-text file written in Gherkin syntax. It is used in Behavior Driven Development (BDD) to define test scenarios for software.

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
Install `feefifofum` from GitHub by running the following command:
```shell
pip install git+https://github.com/rushwerks/feefifofum.git@v0.3.0
```

## Usage
`feefifofum` runs directly on feature files or directories containing feature files.
If directory paths are provided, then feature files in all corresponding subdirectories will also be formatted.

```shell
feefifofum <file>                     # Format a single file
feefifofum <file1> <file2> <file3>    # Format multiple files
feefifofum .                          # Format all feature files in current directory and subdirectories
feefifofum <directory>                # Format all feature files in specified directory and any subdirectories
feefifofum <directory1> <directory2>  # Format all feature files in multiple directories (and any of their subdirectories)
```

### Output
In its default setting, `feefifofum` will only log the total number of formatted and unchanged files to the console.
Files marked as 'unchanged' already meet the required formatting standard. Therefore no changes are written to these files.

The `--verbose` or `-v` flag can be passed to log realtime information on which files have been formatted (or are unchanged), and overall progress.
```shell
feefifofum <file1> <file2> <file3> --verbose
```

### Backup
If files do not meet the required formatting standards, `feefifofum` will overwrite them with necessary changes.

The `--backup` flag can be passed to create backups of the original files.
This works by creating a copy of the original file in the same directory, and appending a `.bak` extension to the filename. Permissions of the original file will be preserved and file metadata will attempt to be [preserved](https://docs.python.org/3/library/shutil.html#shutil.copy2).
```shell
feefifofum <file> --backup --verbose
```

### Dry-run
The `--dry-run` flag can be passed to avoid writing formatted files back.
The number of files that would have been formatted, is then logged to the console after `feefifofum` has run.

It can be combined with the `--debug` flag to produce a list of feature files which would be formatted.
```shell
feefifofum <directory> --dry-run --verbose
```

## Pre-commit
`feefifofum` is also available as a pre-commit hook. It can be configured as follows:
```yaml
  - repo: https://github.com/rushwerks/feefifofum/
    rev: v0.3.0
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

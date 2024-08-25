# feefifofum

<div align='center'>

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)

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
    * Feature: Zero spaces
    * Scenario: Two spaces
    * Given/When/Then: Four spaces
    * Tables/step text: Six spaces

## Usage
Format any number of feature files or directories containing feature files, by providing a list of path arguments. If directory paths are provided, then feature files will be searched recursively downward from these paths.

```shell
feefifofum <file>
feefifofum <file1> <file2> <file3>
feefifofum <directory1> <directory2>
```

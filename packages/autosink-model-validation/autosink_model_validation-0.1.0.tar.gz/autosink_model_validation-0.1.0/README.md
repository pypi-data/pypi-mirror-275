# Model Validation for Autosink Project

[🇬🇧](README.md) | [🇰🇷](README.kr.md) | [🇨🇳](README.zh-CN.md)

The environment is based on MacOS and Linux.

## `Makefile`

The `Makefile` has the following functions.

### `make lint`

- To use the `.vscode` settings, install the `pylint` extension.
- It overrides the options specified in the `pyproject.toml` file in the default settings of the linter and lints the code.

### `make format`

- The formatter uses Google's `yapf`.
- It overrides the options specified in the `pyproject.toml` file in the default settings of the `yapf` formatter and formats the code.
- To use the `.vscode` settings, install the `yapf` extension.

### `make test`

- It uses `unittest` for testing.
- It supports both `test_*.py` and `*_test.py` patterns.
- The test file must be connected to `__init__.py` up to the location where the test file exists.

### `make publish`

- Write the `~/.pypirc` file as follows.
    ```
    [pypi]
    username = __token__
    password = pypi-something # Obtain and write your personal API token.
    ```
- When this command is executed, it pushes the package to the PyPI public registry using `flit`.
- The previously specified name `myproject` (alias) will be uploaded, allowing anyone worldwide to install and use the package with `python3 -m pip install myproject`.
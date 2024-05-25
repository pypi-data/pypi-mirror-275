# Autosink 项目的模型验证

[🇬🇧](README.md) | [🇰🇷](README.kr.md) | [🇨🇳](README.zh-CN.md)

环境以 MacOS、Linux 为基准。

## `Makefile`

`Makefile` 包含以下功能。

### `make lint`

- 若要使用 `.vscode` 设置，请安装 `pylint` 扩展。
- 通过覆盖 linter 的默认设置来对代码进行 lint，使用在 `pyproject.toml` 文件中指定的选项。

### `make format`

- 使用谷歌的 `yapf` 作为格式化工具。
- 通过覆盖 `yapf` 格式化器的默认设置来对代码进行格式化，使用在 `pyproject.toml` 文件中指定的选项。
- 若要使用 `.vscode` 设置，请安装 `yapf` 扩展。

### `make test`

- 使用 `unittest` 进行测试。
- 支持 `test_*.py` 和 `*_test.py` 模式。
- 测试文件必须与 `__init__.py` 相连接到测试文件所在的位置。

### `make publish`

- 请按以下格式编写 `~/.pypirc` 文件。
    ```
    [pypi]
    username = __token__
    password = pypi-xxx # 请获取个人 API 令牌并填写
    ```
- 运行此命令将使用 `flit` 将包推送到 PyPI 公共注册表。
- 上传后，您可以通过指定的名称 `myproject`（别名）在全球范围内使用 `python3 -m pip install myproject` 安装并使用该软件包。
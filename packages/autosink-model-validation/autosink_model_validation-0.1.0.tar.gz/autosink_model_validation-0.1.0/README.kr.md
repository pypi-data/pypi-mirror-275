# Model Validation for Autosink Project

[🇬🇧](README.md) | [🇰🇷](README.kr.md) | [🇨🇳](README.zh-CN.md)

환경은 MacOS, Linux 를 기준으로 합니다.

## `Makefile`

`Makefile`은 다음과 같은 기능들을 가지고 있습니다.

### `make lint`

- `.vscode` 설정을 사용하려면 `pylint` 익스텐션을 설치하세요.
- 린터의 기본 세팅에 `pyproject.toml` 파일에 명시된 옵션을 오버라이딩해 코드를 린팅합니다.

### `make format`

- 포매터는 google의 `yapf`를 사용합니다.
- `yapf` 포매터의 기본 세팅에 `pyproject.toml` 파일에 명시된 옵션을 오버라이딩해 코드를 포매팅합니다.
- `.vscode` 설정을 사용하려면 `yapf` 익스텐션을 설치하세요.

### `make test`

- 테스트는 `unittest`를 사용합니다.
- `test_*.py` 와 `*_test.py` 패턴을 모두 지원합니다.
- 테스트 파일이 존재하는 위치까지 `__init__.py` 로 연결되어 있어야 합니다.

### `make publish`

- `~/.pypirc` 파일을 아래와 같이 작성하세요.
    ```
    [pypi]
    username = __token__
    password = pypi-어쩌고저쩌고 # 개인 API 토큰을 발급받아 작성하세요.
    ```
- 이 명령을 실행하면 `flit` 을 사용하여 PyPI 공개 레지스트리에 패키지를 푸시합니다.
- 앞서 이름으로 지정한 `myproject`(가명)이 업로드되어, 전세계 누구나 `python3 -m pip install myproject`로 패키지를 설치해 사용할 수 있게 됩니다.

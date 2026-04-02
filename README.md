[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=stable)](https://whist-core.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/Whist-Team/Whist-Core/branch/main/graph/badge.svg)](https://codecov.io/gh/Whist-Team/Whist-Core)
![PyPI](https://img.shields.io/pypi/v/whist-core)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/whist-core)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/whist-core)
![GitHub repo size](https://img.shields.io/github/repo-size/whist-team/whist-core)
![Lines of code](https://img.shields.io/tokei/lines/github/whist-team/whist-core)
![PyPI - Downloads](https://img.shields.io/pypi/dm/whist-core)
![PyPI - License](https://img.shields.io/pypi/l/whist-core)

# Whist-Core
Whist rules implementation

## Development

### Setup
You need [uv](https://docs.astral.sh/uv/) for development.
```bash
# Create venv and install deps
uv sync
```
The Python virtual environment will be created in the `.venv` directory.

### Run tests/lint
```bash
# Run tests (in venv)
python -m pytest # or pylint...
# OR
uv run -m pytest
```

### Build
Generates `sdist` and `bdist_wheel`.
```bash
uv build
```

### Publish
You need the environment variable `UV_PUBLISH_TOKEN` filled with a PyPI token.
```bash
uv build
uv publish
```

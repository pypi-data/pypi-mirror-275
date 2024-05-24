# Xemporal

1. wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

## Setting up the runtime environment

```bash
brew install pipx
sudo pipx --global ensurepath
pipx install poetry
pipx install -U pip setuptools
poetry config virtualenvs.in-project true
poetry config virtualenvs.prefer-active-python true
```

## Setting up the project

```bash
virtualenv .venv --python=python3.12
poetry shell
poetry install
poetry build
poetry run pytest
```
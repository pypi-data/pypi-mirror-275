#!/bin/bash

cd "$(dirname "$0")" || exit 1

./build.sh

if [[ ! -d .venv ]]; then
  python -m venv .venv
fi

source .venv/bin/activate
pip install --upgrade twine

python -m twine upload --verbose -u __token__ -p "$PYPI_TOKEN" -r pypi dist/*

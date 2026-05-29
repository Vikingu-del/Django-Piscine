#!/usr/bin/env bash

if [ "$1" == "--fix" ]; then
  ruff check . --fix && black ./chanx_django && toml-sort ./*.toml
else
  ruff check . && black ./chanx_django --check && toml-sort ./*.toml --check
fi

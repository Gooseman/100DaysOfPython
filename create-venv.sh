#!/bin/bash

echo Working in
pwd

echo Creating virtual environment venv
python -m venv .venv

echo Switching to venv
source .venv/Scripts/activate

.venv/Scripts/python -m pip install --upgrade pip
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/pre-commit install --install-hooks --hook-type pre-commit

echo Checking current virtual environment
echo $VIRTUAL_ENV

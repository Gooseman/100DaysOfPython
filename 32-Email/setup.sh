#!/bin/bash

python -m venv .venv
source .venv/Scripts/activate

python -m pip install -e .

#!/bin/bash

echo Working in
pwd

echo Creating virtual environment venv
python -m venv venv

echo Switching to venv
source venv/Scripts/activate

echo Checking current virtual environment
echo $VIRTUAL_ENV

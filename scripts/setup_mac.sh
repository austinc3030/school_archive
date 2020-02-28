#!/bin/bash

npm install
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
# ./build.sh

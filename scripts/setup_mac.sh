#!/bin/bash

npm install
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
# ./build.sh

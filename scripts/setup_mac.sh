#!/bin/bash

# Install node stuff
npm install

# Setup Python Stuff
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
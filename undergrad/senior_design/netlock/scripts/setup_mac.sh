#!/bin/bash

# Export variable to ensure the proper version of chrome is downloaded
export CHROMIUM_REVISION=722274

# Install node stuff
npm install

# Setup Python Stuff
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate

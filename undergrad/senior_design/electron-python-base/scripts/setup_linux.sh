#!/bin/bash

# Install necessary packages
sudo apt-get -y install dpkg fakeroot

# Install node modules
npm install

# Setup Python Stuff
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate
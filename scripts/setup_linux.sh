#!/bin/bash

sudo apt-get -y install dpkg fakeroot
npm install
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
deactivate

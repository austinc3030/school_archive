#!/bin/bash
# Cleanup previous build
rm -rf out/
rm -rf python/build/ 
rm -rf python/dist/
rm -rf python/__pycache__/
rm -rf py_out/

# Build python stuff
source .venv/bin/activate
pyinstaller python/python.spec --distpath py_out --workpath python/build --specpath python/ --onefile 
deactivate

# Build and package
npm run make

# Open app
open out/electron-python-base-darwin-x64/electron-python-base.app/

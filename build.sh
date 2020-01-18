#!/bin/bash
# Cleanup previous build
rm -rf out/
rm -rf py_src/build/ 
rm -rf py_src/dist/
rm -rf py_src/__pycache__/
rm -rf py_src/*.spec
rm -rf py_out/

# Build python stuff
source .venv/bin/activate
pyinstaller py_src/pytest1.py --distpath py_out --workpath py_src/build --specpath py_src/ --onefile 
deactivate

# Build and package
npm run make

# Open app
open out/electron-python-base-darwin-x64/electron-python-base.app/

#!/bin/bash
# Cleanup previous build
rm -rf out/
rm -rf py_src/build/ 
rm -rf py_src/dist/
rm -rf py_src/__pycache__/
rm -rf py_out/

# Build python stuff
source .venv/bin/activate
pyinstaller py_src/api.spec --distpath py_out
deactivate

# Build and package
npm run make
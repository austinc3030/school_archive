#!/bin/bash
# Cleanup previous build
rm -rf out/
rm -rf build/ 
rm -rf backend_src/__pycache__/
rm -rf backend/

# Build python stuff
source .venv/bin/activate
pyinstaller backend_src/api.spec --distpath backend
deactivate

# Build and package
npm run make

# Open app
open out/netlock-darwin-x64/netlock.app/

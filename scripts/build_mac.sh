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

# Needed to make sure chromium runs headless and doesn't show the chromium icon in the dock
# Commented for now. Needs to be uncommented for deployment
# defaults write /Users/austinc/GitHub/netlock/node_modules/chromium/lib/chromium/chrome-mac/Chromium.app/Contents/Info.plist LSBackgroundOnly -string '1'

# Build and package
npm run make

# Reverse change to plist so we can test.
# Ideally, both of these statements would be uncommented so that we still track the package version of
# Chromium. However, need this removed for testing so we can see the window.
defaults delete /Users/austinc/GitHub/netlock/node_modules/chromium/lib/chromium/chrome-mac/Chromium.app/Contents/Info.plist LSBackgroundOnly

# Open app
rm -rf /Applications/netlock.app
cp -R out/netlock-darwin-x64/netlock.app /Applications/
open /Applications/netlock.app/

Set-ExecutionPolicy Unrestricted -Scope process -Force

# Export variable to ensure the proper version of chrome is downloaded
$env:CHROMIUM_REVISION=722274

# Install node modules
npm install

# Setup python stuff
virtualenv.exe -p python3 .venv
.\.venv\Scripts\activate.ps1
pip install -r .\requirements_win.txt
deactivate

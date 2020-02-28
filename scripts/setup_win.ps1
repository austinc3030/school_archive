Set-ExecutionPolicy Unrestricted -Scope process -Force

# Install node modules
npm install

# Setup python stuff
virtualenv.exe -p python3 .venv
.\.venv\Scripts\activate.ps1
pip install -r .\requirements_win.txt
deactivate

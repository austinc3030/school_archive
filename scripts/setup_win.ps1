Set-ExecutionPolicy Unrestricted -Scope process -Force
npm install
virtualenv.exe .venv
.\.venv\Scripts\activate.ps1
pip install -r .\requirements.txt
deactivate

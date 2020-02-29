# Needed to enable scripts
Set-ExecutionPolicy Unrestricted -Scope process -Force

# Remove previous build outputs
Remove-Item "netlock-setup.exe" -Force -Recurse -ErrorAction Ignore
Remove-Item "out" -Force -Recurse -ErrorAction Ignore
Remove-Item "backend" -Force -Recurse -ErrorAction Ignore
Remove-Item "build" -Force -Recurse -ErrorAction Ignore
Remove-Item "backend_src\__pycache__" -Force -Recurse -ErrorAction Ignore

# Build python part
.\.venv\Scripts\activate.ps1
pyinstaller backend_src/api.spec --distpath backend
deactivate

# Build it
npm run package

# Build the installer
& 'C:\Program Files (x86)\Inno Setup 6\ISCC.exe' /q .\scripts\inno_builder_script.iss
cp .\out\netlock-setup.exe ./netlock-setup.exe

# Run the installer
Start-Process -FilePath .\netlock-setup.exe
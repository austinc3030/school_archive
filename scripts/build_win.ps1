# Needed to enable scripts
Set-ExecutionPolicy Unrestricted -Scope process -Force

# Remove previous build outputs
Remove-Item "epb-setup.exe" -Force -Recurse -ErrorAction Ignore
Remove-Item "out" -Force -Recurse -ErrorAction Ignore
Remove-Item "py_out" -Force -Recurse -ErrorAction Ignore

# Build python part
.\.venv\Scripts\activate.ps1
pyinstaller py_src/pytest1.py --distpath py_out --workpath py_src/build --specpath py_src/ --onefile
deactivate

# Build it
npm run package

# Start the output for testing
# Start-Process -FilePath .\out\electron-python-base-win32-ia32\electron-python-base.exe

# Build the installer
& 'C:\Program Files (x86)\Inno Setup 6\ISCC.exe' /q .\scripts\inno_builder_script.iss
cp .\scripts\Output\electron-python-base.exe ./epb-setup.exe
Remove-Item "scripts\Output" -Force -Recurse -ErrorAction Ignore

# Run the installer
Start-Process -FilePath .\epb-setup.exe

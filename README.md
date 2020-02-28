Dependenices for building (All OS's)
<br>	* Python ( Requires Python 3 )
<br>    * Virtualenv
<br>	* NodeJS ( Requires 12.16.1 )

Additional dependencies for building (Windows)
<br>    * Git
<br>    * Inno Setup (https://www.jrsoftware.org/isinfo.php)

Steps:
<br>	1.) Clone the repo
<br>	2.) cd netlock
<br>    3.) Depending on OS, run script in the /scripts directory
<br> NOTE: Setup scripts are meant to help get the environment setup.

Note on Windows Power Shell Scripts: 
<br> In order to use the .ps1 scripts, you must run `Set-ExecutionPolicy Unrestricted -Scope process -Force` to enable running scripts. This needs to be run any time you start a new poweshell session.

When Adding npm Packages (Either by `npm install` or adding to package.json) After "Steps" (Needs to update the package-lock.json file)
<br>	npm install
<br>	rm -rf node_modules
<br>	npm install

Probably need to add more to this.

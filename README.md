# InstantFTP_PY
A  Simple Python application FTP server for sharing current folder with fast startup and multiconnection boosts for faster transmission.
![ftpy demo in windows powershell](https://raw.githubusercontent.com/devvratmiglani/InstantFTP_PY/main/ftpy-powershell-demo.png)
## Installation
Install as: 
```sh
git clone https://github.com/devvratmiglani/InstantFTP_PY.git
cd InstantFTP_PY
pip install -e .
```
It is now installed in editable mode using the '-e' parameter, using this you can change the the credentials in **`InstantFTP_PY\ftpy\__init__.py`**

## Usage
Run in temrinal as:
```sh
ftpy
```
It will share the current folder of the session on your local network

### Bug
QR is Displayed as blank in some terminals including windows, it can be fixed by running script as unbuffered, pip package might not do that but it could be done by compiling to executable as shown in [InstantFTP](https://github.com/devvratmiglani/InstantFTP), to be noted it should work fine on linux as tested, due to the fact shebang works on linux
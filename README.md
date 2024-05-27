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
It is now installed in editable mode using the '-e' parameter, using this you can change the the credentials in `InstantFTP_PY\ftpy\__init__.py`

or
```sh
pip install git+https://github.com/devvratmiglani/InstantFTP_PY.git
```

## Usage
Run in temrinal as:
```sh
ftpy
```
port already in use?
```sh
ftpy -p 2122
```
It will share the current folder of the session on your local network.

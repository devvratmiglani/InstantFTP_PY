from setuptools import setup

setup(
    name="ftpy",
    version="1.5.0",
    description="A Simple Python application FTP server for sharing current folder with fast startup and multiconnection boosts for faster transmission.",
    url="https://github.com/devvratmiglani",
    author="Devvrat Miglani",
    author_email="devvratmiglani@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["ftpy"],
    install_requires=[
        "pyftpdlib",
        "findmyip",
        "colorama",
        "segno",
    ],
    entry_points = {
        'console_scripts':[
            'ftpy=ftpy:main',
        ],
    },
)

#!/usr/bin/env python -u
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from FindMyIP import internal
from colorama import Fore
import segno
import sys

def main():
    # Set up an authorizer with a user and password
    authorizer = DummyAuthorizer()
    authorizer.add_user("username", "password", ".", perm="elradfmw")
    authorizer.add_user("vlc", "password", ".", perm="elradfmw") ## adds user with password
    authorizer.add_anonymous(".") ## adds anonymous user

    # Instantiate the FTP handler with the given authorizer
    handler = FTPHandler
    handler.passive_ports = range(60000, 65535)
    handler.authorizer = authorizer
    handler.recv_buffer_size = 4096  # Adjust buffer size as needed
    handler.send_buffer_size = 4096  # Adjust buffer size as needed


    # Create and start the FTP server
    hostip = internal()
    server = ThreadedFTPServer((hostip, 2121), handler)
    print(f"{Fore.GREEN}[+] FTP server running at ftp://username:password@{hostip}:2121{Fore.RESET}")
    qr = segno.make(f"ftp://username:password@{internal()}:2121")
    qr.terminal(border=3)
    server.max_cons = 256
    server.max_cons_per_ip = 20
    server.serve_forever()

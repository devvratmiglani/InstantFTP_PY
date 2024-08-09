#!/usr/bin/env python3 -u
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer
from FindMyIP import internal
from colorama import Fore
import argparse
import segno
import sys
import os

def main():
    if os.name == "nt":
        class Unbuffered:
            def __init__(self, stream):
                self.stream = stream

            def write(self, data):
                self.stream.write(data)
                self.stream.flush()

            def flush(self):
                self.stream.flush()

        sys.stdout = Unbuffered(sys.stdout)
        sys.stderr = Unbuffered(sys.stderr)

    parser = argparse.ArgumentParser(description='InstantFTP_PY - A blazingly performant FTP Server')
    parser.add_argument('--port','-p',help='Port to start server on (default 2121)')
    args = parser.parse_args()
    port = 2121
    if args.port is not None:
    	port = args.port

    # Set up an authorizer with a user and password
    authorizer = DummyAuthorizer()
    authorizer.add_user("username", "password", ".", perm="elradfmw")
    authorizer.add_anonymous(".") ## adds anonymous user read only

    # Instantiate the FTP handler with the given authorizer
    handler = FTPHandler
    handler.passive_ports = range(60000, 65535)
    handler.authorizer = authorizer
    handler.recv_buffer_size = 4096  # Adjust buffer size as needed
    handler.send_buffer_size = 4096  # Adjust buffer size as needed


    # Create and start the FTP server
    hostip = internal()
    server = ThreadedFTPServer((hostip, port), handler)
    print(f"{Fore.GREEN}[+] FTP server running at ftp://username:password@{hostip}:{port}{Fore.RESET}")
    qr = segno.make(f"ftp://{internal()}:{port}")
    qr.terminal(border=3)
    server.max_cons = 256
    server.max_cons_per_ip = 20
    server.serve_forever()

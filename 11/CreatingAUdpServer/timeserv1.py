#!/usr/bin/env python3
from socketserver import BaseRequestHandler, UDPServer
import signal
import time
import sys


class TimeHandler(BaseRequestHandler):
    def handle(self) -> None:
        print(f"Got connection from {self.client_address}")
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode("ascii"), self.client_address)


def sighandler(num, arg):
    if num == signal.SIGINT:
        sys.exit(0)


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, sighandler)
    server = UDPServer(("", 20000), TimeHandler)
    print("Server connected on port 20000 ...")
    server.serve_forever()


if __name__ == "__main__":
    main()

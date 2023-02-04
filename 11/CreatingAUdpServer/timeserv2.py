#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_DGRAM
import signal
import time
import sys


def sighandler(signum, arg):
    if signum==signal.SIGINT:
        sys.exit(0)


def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print(f"Got message from {addr}")
        response = time.ctime()
        sock.sendto(response.encode("utf-8"), addr)


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, sighandler)
    time_server(("", 20000))


if __name__ == "__main__":
    main()

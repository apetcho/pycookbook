#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, stype=SOCK_STREAM):
        self.address = address
        self.family = family
        self.stype = stype
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connected")
        self.sock = socket(self.family, self.stype)
        self.sock.connect(self.address)
        return self.sock
    
    def __exit__(self, excty, excval, tb):
        self.sock.close()
        self.sock = None


def main():
    """Main entry."""
    conn = LazyConnection(("www.python.org", 80))
    # -*-
    with conn as sock:
        sock.send(b"GET /index.html HTTP/1.0\r\n")
        sock.send(b"Host: www.python.org\r\n")
        sock.send(b"\r\n")
        response = b"".join(iter(partial(sock.recv, 8192), b""))

    print(f"Got {len(response)} bytes")


if __name__ == "__main__":
    main()

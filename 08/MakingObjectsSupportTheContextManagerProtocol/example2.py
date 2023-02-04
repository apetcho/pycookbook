#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.stype = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.stype)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock
    
    def __exit__(self, excty, excval, tb):
        self.connections.pop().close()


def main():
    """Main entry."""
    conn = LazyConnection(("www.python.org", 80))
    with conn as sock:
        sock.send(b"GET /index.html HTTP/1.0\r\n")
        sock.send(b"Host: www.python.org\r\n")
        sock.send(b"\r\n")
        response = b"".join(iter(partial(sock.recv, 8192), b""))

    print(f"Got {len(response)} bytes")

    with conn as sock1, conn as sock2:
        sock1.send(b"GET /index.html HTTP/1.0\r\n")
        sock2.send(b"GET /index.html HTTP/1.0\r\n")
        sock1.send(b"Host: www.python.org\r\n")
        sock2.send(b"Host: www.python.org\r\n")
        sock1.send(b"\r\n")
        sock2.send(b"\r\n")
        response1 = b"".join(iter(partial(sock1.recv, 8192), b""))
        response2 = b"".join(iter(partial(sock2.recv, 8192), b""))

    print(f"Response-1 got {len(response1)} bytes")
    print(f"Response-2 got {len(response2)} bytes")


if __name__ == "__main__":
    main()

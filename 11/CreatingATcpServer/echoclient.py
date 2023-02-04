#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM


def main():
    """Main entry."""
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(("localhost", 20000))
    sock.send(b"Hello\n")
    resp = sock.recv(8192)
    print(f"Response: {resp}")
    sock.close()


if __name__ == "__main__":
    main()

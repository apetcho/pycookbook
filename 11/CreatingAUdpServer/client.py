#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_DGRAM


def main():
    """Main entry."""
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.sendto(b"", ("localhost", 20000))
    print(sock.recvfrom(8192)) #.decode("utf-8"))


if __name__ == "__main__":
    main()

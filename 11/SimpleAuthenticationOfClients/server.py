#!/usr/bin/env python3
import sys
import signal
from socket import socket, AF_INET, SOCK_STREAM
from auth import server_authenticate


def _sighandler(num, args):
    if num == signal.SIGINT:
        sys.exit(0)


class Server:
    SECRET_KEY = b"peekaboo"

    def __init__(self):
        self.__secret_key = self.SECRET_KEY

    def echo_handler(self, client_sock:socket):
        if not server_authenticate(client_sock, self.__secret_key):
            client_sock.close()
            return
        while True:
            msg = client_sock.recv(8192)
            if not msg:
                break
            client_sock.sendall(msg)

    def server_forever(self, address):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.bind(address)
        sock.listen(5)
        while True:
            conn, addr = sock.accept()
            print(f"Received request from {addr}")
            self.echo_handler(conn)


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, _sighandler)
    # -*-
    server = Server()
    print("Echo server running on port 18000")
    server.server_forever(("", 18000))


if __name__ == "__main__":
    main()

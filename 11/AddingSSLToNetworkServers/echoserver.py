#!/usr/bin/env python3
from socket import socket, AF_INET, SOCK_STREAM
from socket import SOL_SOCKET, SO_REUSEADDR
import ssl

# -*- Private key of the server -*-
KEYFILE = "server_key.pem"
# -*- Server certificate (given to client) -*-
CERTFILE = "server_cert.pem"


def echo_client(sock:socket):
    while True:
        data = sock.recv(8192)
        if data == b"":
            break
        sock.send(data)
    sock.close()
    print("Connection closed")


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    # -*- Wrap with an SSL layer requiring client certs
    ssl_sock = ssl.wrap_socket(
        sock, keyfile=KEYFILE, certfile=CERTFILE, server_side=True
    )
    # -*- Wait for connections -*-
    while True:
        try:
            conn, addr = ssl_sock.accept()
            print(f"Got connection ({conn}, {addr})")
            echo_client(conn)
        except Exception as err:
            print(f"{err.__class__.__name__}: {err}")


def main():
    """Main entry."""
    echo_server(("", 20000))


if __name__ == "__main__":
    main()

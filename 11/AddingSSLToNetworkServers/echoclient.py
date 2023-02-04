#!/usr/bin/env python3
"""An example of a client that connects to an SSL server and verifies its
certificate.
"""
from socket import socket, AF_INET, SOCK_STREAM
import ssl


def main():
    """Main entry."""
    sock = socket(AF_INET, SOCK_STREAM)
    # Wrap with an SSL layer and require the server to present its certificate
    ssl_sock = ssl.wrap_socket(
        sock, cert_reqs=ssl.CERT_REQUIRED,
        ca_certs="server_cert.pem",
    )
    ssl_sock.connect(("localhost", 20000))

    # Communicate with the server
    ssl_sock.send(b"Hello World!")
    response = ssl_sock.recv(8192)
    print(f"Got: {response}")
    # Done
    ssl_sock.close()


if __name__ == "__main__":
    main()

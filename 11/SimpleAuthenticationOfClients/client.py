from socket import socket, AF_INET, SOCK_STREAM
from auth import client_authenticate


def main():
    """Main entry."""
    SECRET_KEY = b"peekaboo"
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(("localhost", 18000))
        client_authenticate(sock, SECRET_KEY)
        sock.send(b"Hello World")


if __name__ == "__main__":
    main()

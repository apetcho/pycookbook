#!/usr/bin/env python3
from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self) -> None:
        print(f"Got connection from {self.client_address}")
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


def main():
    """Main entry."""
    server = TCPServer(("", 20000), EchoHandler)
    print("Echo server running on port 20000")
    server.serve_forever()


if __name__ == "__main__":
    main()

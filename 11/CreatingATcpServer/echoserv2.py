#!/usr/bin/env python3
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    def handle(self) -> None:
        print(f"Got connection from {self.client_address}")
        for line in self.rfile:
            self.wfile.write(line)


def main():
    """Main entry."""
    server = TCPServer(("", 20000), EchoHandler)
    print("Echo server running on port 20000")
    server.serve_forever()


if __name__ == "__main__":
    main()

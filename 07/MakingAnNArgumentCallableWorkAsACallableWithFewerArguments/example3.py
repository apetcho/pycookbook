#!/usr/bin/env python3
from socketserver import StreamRequestHandler, TCPServer


class EchoHandler(StreamRequestHandler):
    """EchoHandler class."""
    # ack is added keyword-only argument. *args, **kwargs are
    # any normal parameters supplied (which are passed on)

    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self) -> None:
        for line in self.rfile:
            self.wfile.write(self.ack + line)


def main():
    """Main entry."""
    from functools import partial

    server = TCPServer(("", 15000), partial(EchoHandler, ack=b"RECEIVED:"))
    print("Echo server running on port 15000")
    server.serve_forever()


if __name__ == "__main__":
    main()

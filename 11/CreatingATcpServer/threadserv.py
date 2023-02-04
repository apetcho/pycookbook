#!/usr/bin/env python3
from socketserver import StreamRequestHandler, TCPServer
from threading import Thread
import socket
import signal
import sys


def sighandler(num, args):
    if num == signal.SIGINT:
        sys.exit(0)


class EchoHandler(StreamRequestHandler):
    def handle(self) -> None:
        print(f"Got connection from {self.client_address}")
        for line in self.rfile:
            self.wfile.write(line)


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, sighandler)
    NWORKERS = 16
    server = TCPServer(("", 20000), EchoHandler)
    # server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    for _ in range(NWORKERS):
        thd = Thread(target=server.serve_forever)
        thd.daemon = True
        thd.start()
    print("Multithreaded server running on port 20000")
    server.serve_forever()


if __name__ == "__main__":
    main()

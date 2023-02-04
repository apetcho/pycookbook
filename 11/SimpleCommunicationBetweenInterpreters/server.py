#!/usr/bin/env python3
import sys
import signal
import traceback
from multiprocessing.connection import Listener


def _sighandler(num, arg):
    if num==signal.SIGINT:
        sys.exit(0)


def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print("Connection closed")


def echo_server(address, authkey):
    server = Listener(address, authkey=authkey)
    while True:
        try:
            client = server.accept()
            print(f"Received: {client}")
            echo_client(client)
        except Exception:
            traceback.print_exc()


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, _sighandler)
    echo_server(("", 25000), authkey=b"peekaboo")


if __name__ == "__main__":
    main()

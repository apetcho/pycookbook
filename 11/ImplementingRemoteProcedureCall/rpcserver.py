#!/usr/bin/env python3
import sys
import signal
import pickle
from threading import Thread
from multiprocessing.connection import Listener


def _sighandler(num, args):
    if num == signal.SIGINT:
        sys.exit(0)


class RPCHandler:
    def __init__(self):
        pass

    def register_function(self, fun):
        pass

    def handler_connection(self, connection):
        pass


def rpc_server(handler:RPCHandler, address, authkey):
    """RPC Server"""
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        thd = Thread(target=handler.handler_connection, args=(client,))
        thd.daemon = True
        thd.start()


# -*-

def main():
    """Main entry."""
    signal.signal(signal.SIGINT, _sighandler)
    functions = {}
    functions["add"] = (lambda x, y: x + y)
    functions["sub"] = (lambda x, y: x - y)
    # -*-
    handler = RPCHandler()
    handler.register_function(functions["add"])
    handler.register_function(functions["sub"])
    # -*-
    rpc_server(handler, ("localhost", 17000), authkey=b"peekaboo")


if __name__ == "__main__":
    main()

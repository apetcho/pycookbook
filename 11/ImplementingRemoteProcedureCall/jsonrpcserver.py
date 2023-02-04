#!/usr/bin/env python3
import sys
import signal
import json
from typing import Callable
from threading import Thread
from multiprocessing.connection import Listener


def _sighandler(num, args):
    if num == signal.SIGINT:
        sys.exit(0)


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, fun:Callable):
        self._functions[fun.__name__] = fun

    def handler_client(self, connection):
        try:
            while True:
                fun_name, args, kwargs = json.loads(connection.recv)
                try:
                    result = self._functions[fun_name](*args, **kwargs)
                    connection.send(json.dumps(result))
                except Exception as err:
                    connection.send(json.dumps(str(err)))
        except EOFError:
            pass


def rpc_server(handler:RPCHandler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        thd = Thread(target=handler.handler_client, args=(client,))
        thd.daemon = True
        thd.start()


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def main():
    """Main entry."""
    signal.signal(signal.SIGINT, _sighandler)
    # -*- Register with a handler
    handler = RPCHandler()
    handler.register_function(add)
    handler.register_function(sub)

    # -*- Run the server
    rpc_server(handler, ("localhost", 17000), authkey=b"peekaboo")


if __name__ == "__main__":
    main()

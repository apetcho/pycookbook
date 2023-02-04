#!/usr/bin/env python3
import json
from multiprocessing.connection import Client


class RPCProxy:
    def __init__(self, connection):
        self._connection = connection

    def __getattr__(self, name):
        def do_rpc(*args, **kwargs):
            self._connection.send(json.dumps((name, args, kwargs)))
            result = json.loads(self._connection.recv())
            return result
        return do_rpc
    

def main():
    """Main entry."""
    client = Client(("localhost", 17000), authkey=b"peekaboo")
    proxy = RPCProxy(client)
    print(proxy.add(2, 3))
    print(proxy.sub(2, 3))
    try:
        print(proxy.sub([1, 2], 4))
    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()

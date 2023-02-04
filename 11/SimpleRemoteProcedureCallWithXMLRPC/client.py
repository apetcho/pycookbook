#!/usr/bin/env python3
from xmlrpc.client import ServerProxy


def main():
    """Main entry."""
    proxy = ServerProxy("http://localhost:15000", allow_none=True)
    proxy.set("foo", "bar")
    proxy.set("spam", [1, 2, 3])
    print(proxy.keys())
    print(proxy.get("foo"))
    print(proxy.get("spam"))
    proxy.delete("spam")
    print(proxy.exits("spam"))


if __name__ == "__main__":
    main()

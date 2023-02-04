#!/usr/bin/env python3
from multiprocessing.connection import Client

def main():
    """Main entry."""
    conn = Client(("localhost", 25000), authkey=b"peekaboo")
    conn.send("hello")
    print(f"Got: {conn.recv()}")
    conn.send(42)
    print(f"Got: {conn.recv()}")
    conn.send([1, 2, 3, 4, 5])
    print(f"Got: {conn.recv()}")


if __name__ == "__main__":
    main()

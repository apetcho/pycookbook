#!/usr/bin/env python3
from io import FileIO
from struct import Struct


def read_records(fmt:str, fp:FileIO):
    record_struct = Struct(fmt)
    chunks = iter(lambda: fp.read(record_struct.size), b"")
    return (record_struct.unpack(chunk) for chunk in chunks)


def main():
    """Main entry."""
    import os
    filename = os.path.join(os.path.dirname(__file__), "data.b")
    with open(filename, "rb") as fp:
        for record in read_records("<idd", fp):
            print(record)


if __name__ == "__main__":
    main()

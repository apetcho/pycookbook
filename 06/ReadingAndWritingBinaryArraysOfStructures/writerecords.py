#!/usr/bin/env python3
from io import FileIO
from struct import Struct
from typing import Collection, Tuple


def write_records(records:Collection[Tuple], format:str, fp:FileIO):
    """Write a sequence of tuples to a binary file of structures."""
    records_struct = Struct(format)
    for record in records:
        fp.write(records_struct.pack(*record))


def main():
    """Main entry."""
    import os
    records = [
        (1, 2.3, 4.5),
        (6, 7.8, 9.0),
        (12, 13.4, 56.7),
    ]
    filename = os.path.join(os.path.dirname(__file__), "data.b")
    with open(filename, "wb") as fp:
        write_records(records, "<idd", fp)


if __name__ == "__main__":
    main()

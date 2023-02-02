#!/usr/bin/env python3
"""Example of iterating of fixed-size records."""
# The file 'data.bin' contains 32-byte fixed size records that consists of
# a 4-digit number followed by a 28-byte string.
from functools import partial


def main():
    """Main entry."""
    RECORD_SIZE = 32
    import os
    fname = os.path.join(os.path.dirname(__file__), "data.bin")

    with open(fname, "rb") as fp:
        records = iter(partial(fp.read, RECORD_SIZE), b"")
        for record in records:
            print(record)


if __name__ == "__main__":
    main()

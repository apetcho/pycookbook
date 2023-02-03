#!/usr/bin/env python3
from struct import Struct


def unpack_records(fmt:str, data):
    record_struct = Struct(fmt)

    return (
        record_struct.unpack_from(data, offset)
        for offset in range(0, len(data), record_struct.size)
    )


def main():
    """Main entry."""
    import os
    filename = os.path.join(os.path.dirname(__file__), "data.b")
    with open(filename, "rb") as fp:
        data = fp.read()
        for record in unpack_records("<idd", data):
            print(record)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import struct


def _get_filepath() -> str:
    import os
    filename = os.path.join(os.path.dirname(__file__), "polys.bin")
    return filename


class StructFied:
    def __init__(self, fmt:str, offset:int):
        self.fmt = fmt
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            entry = struct.unpack_from(self.fmt, instance._buffer, self.offset)
            return entry[0] if len(entry) == 1 else entry


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


def main():
    """Main entry."""
    

    class PolyHeader(Structure):
        fileCode = StructFied("<i", 0)
        xmin = StructFied("<d", 4)
        ymin = StructFied("<d", 12)
        xmax = StructFied("<d", 20)
        ymax = StructFied("<d", 28)
        numPolys = StructFied("<i", 36)

    with open(_get_filepath(), "rb") as fp:
        data = fp.read()
        phead = PolyHeader(data)
        print(phead.fileCode == 0x1234)
        print(f"xmin = {phead.xmin}")
        print(f"xmax = {phead.xmax}")
        print(f"ymin = {phead.ymin}")
        print(f"ymax = {phead.ymax}")
        print(f"numPolys = {phead.numPolys}")


if __name__ == "__main__":
    main()



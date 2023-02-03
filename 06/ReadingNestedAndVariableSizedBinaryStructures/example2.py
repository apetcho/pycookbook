#!/usr/bin/env python3
from io import FileIO
import struct


def _getfile() -> str:
    import os
    return os.path.join(os.path.dirname(__file__), "polys.bin")


class StructField:
    def __init__(self, fmt:str, offset:int):
        self.fmt = fmt
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = struct.unpack_from(self.fmt, instance._buffer, self.offset)
            return data[0] if len(data) == 1 else data


class StructureMeta(type):
    """Metaclass that automatically creates StructField descriptors."""

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, "_fields_", [])
        byteOrder = ""
        offset = 0
        for fmt, fieldname in fields:
            if fmt.startswith(("<", ">", "!", "@")):
                byteOrder = fmt[0]
                fmt = fmt[1:]
            fmt = byteOrder + fmt
            setattr(self, fieldname, StructField(fmt, offset))
            offset += struct.calcsize(fmt)
        setattr(self, "struct_size", offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, fp:FileIO):
        return cls(fp.read(cls.struct_size))


def main():
    """Main entry."""

    class PolyHeader(Structure):
        _fields_ = [
            ("<i", "fileCode"),
            ("d", "xmin"),
            ("d", "ymin"),
            ("d", "xmax"),
            ("d", "ymax"),
            ("i", "numPolys")
        ]

    with open(_getfile(), "rb") as fp:
        phead = PolyHeader.from_file(fp)
        print(phead.fileCode == 0x1234)
        print(f"xmin = {phead.xmin}")
        print(f"xmax = {phead.xmax}")
        print(f"ymin = {phead.ymin}")
        print(f"ymax = {phead.ymax}")
        print(f"numPolys = {phead.numPolys}")


if __name__ == "__main__":
    main()

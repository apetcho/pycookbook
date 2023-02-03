#!/usr/bin/env python3
from io import FileIO
import struct


def _getfile():
    import os
    return os.path.join(os.path.dirname(__file__), "polys.bin")


class StructField:
    """Descriptor representing a simple structure field."""

    def __init__(self, fmt, offset):
        self.fmt = fmt
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = struct.unpack_from(self.fmt, instance._buffer, self.offset)
            return data[0] if len(data)==1 else data


class NestedStruct:
    """Descriptor representing a nested structure."""

    def __init__(self, name, stype, offset):
        self.name = name
        self.stype = stype
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[
                self.offset:(self.offset+self.stype.struct_size)
            ]
            result = self.stype(data)
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    """Metaclass that automatically creates StructField descriptors"""

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, "_fields_", [])
        byteOrder = ""
        offset = 0
        for fmt, fieldname in fields:
            if isinstance(fmt, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, fmt, offset))
                offset += fmt.struct_size
            else:
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

    class Point(Structure):
        _fields_ = [("<d", "x"), ("d", "y")]

    class PolyHeader(Structure):
        _fields_ = [
            ("<i", "fileCode"), (Point, "min"),
            (Point, "max"), ("i", "numPolys")
        ]

    # -*-
    with open(_getfile(), "rb") as fp:
        phead = PolyHeader.from_file(fp)
        print(phead.fileCode == 0x1234)
        print(f"xmin = {phead.min.x}")
        print(f"xmax = {phead.max.x}")
        print(f"ymin = {phead.min.y}")
        print(f"ymax = {phead.max.y}")
        print(f"numPolys = {phead.numPolys}")


if __name__ == "__main__":
    main()

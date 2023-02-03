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
    """Metaclass that automatically creates StructField descriptors."""

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, "_fields_", [])
        byteOder = ""
        offset = 0
        for fmt, fieldname in fields:
            if isinstance(fmt, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, fmt, offset))
                offset += fmt.struct_size
            else:
                if fmt.startswith(("<", ">", "!", "@")):
                    byteOder = fmt[0]
                    fmt = fmt[1:]
                fmt = byteOder + fmt
                setattr(self, fieldname, StructField(fmt, offset))
                offset += struct.calcsize(fmt)
        setattr(self, "struct_size", offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, fp:FileIO):
        return cls(fp.read(cls.struct_size))


class SizeRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    @classmethod
    def from_file(cls, fp:FileIO, sizefmt, includesSize=True):
        szNBytes = struct.calcsize(sizefmt)
        szBytes = fp.read(szNBytes)
        sz, = struct.unpack(sizefmt, szBytes)
        buf = fp.read(sz - includesSize*szNBytes)
        return cls(buf)
    
    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for offset in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, offset)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for offset in range(0, len(self._buffer), size):
                data = self._buffer[offset:(offset+size)]
                yield code(data)


def main():
    """Main entry."""

    class Point(Structure):
        _fields_ = [("<d", "x"), ("d", "y")]

    class PolyHeader(Structure):
        _fields_ = [
            ("<i", "fileCode"), (Point, "min"),
            (Point, "max"), ("i", "numPolys")
        ]

    def read_polys(filename):
        polys = []
        with open(filename, "rb") as fp:
            phead = PolyHeader.from_file(fp)
            for _ in range(phead.numPolys):
                record = SizeRecord.from_file(fp, "<i")
                poly = [(point.x, point.y) for point in record.iter_as(Point)]
                polys.append(poly)
        return polys
    
    polys = read_polys(_getfile())
    print(polys)


if __name__ == "__main__":
    main()

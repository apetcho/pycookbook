#!/usr/bin/env python3
# -*- Defining a simple abstract base class -*-
from abc import ABC, abstractmethod
import sys
import io


class IStream(ABC):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


# -*--------------------------*-
# -*- Example implementation -*-
# -*--------------------------*-

class SocketStream(IStream):
    
    def read(self, maxbytes=-1):
        print("reading")

    def write(self, data):
        print("writing")


# -*----------------------------*-
# -*- Example of type checking -*-
# -*----------------------------*-

def serialize(obj, stream:IStream):
    if not isinstance(stream, IStream):
        raise TypeError("Expected an IStream")
    print("serializing")


def main():
    """Main entry."""
    # -*- Examples -*-
    try:
        istrm = IStream()
    except TypeError as err:
        print(err)

    # -*- Instantiation of a concrete implementation -*-
    sockstrm = SocketStream()
    sockstrm.read()
    sockstrm.write("data")

    # -*- Passing to type-check function -*-
    serialize(None, sockstrm)

    # -*- Attempt to pass a file-like object to serialize (fails)
    try:
        serialize(None, sys.stdout)
    except TypeError as err:
        print(err)

    # -*- Register file streams and retry -*-
    IStream.register(io.IOBase)

    serialize(None, sys.stdout)


if __name__ == "__main__":
    main()

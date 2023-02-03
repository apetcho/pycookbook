#!/usr/bin/env python3
# -*- Class decorator alternative to mixins -*-

def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print(f"Getting {key}")
        return cls_getitem(self, key)
    
    def __setitem__(self, key, value):
        print(f"Setting {key!s} = {value!r}")
        return cls_setitem(self, key, value)
    
    def __delitem__(self, key):
        print(f"Deleting {key:s}")
        return cls_delitem(self, key)
    
    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDict(dict):
    pass


def main():
    """Main entry."""
    dct = LoggedDict()
    dct["x"] = 23
    print(dct["x"])
    del dct["x"]


if __name__ == "__main__":
    main()

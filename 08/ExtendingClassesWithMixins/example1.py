#!/usr/bin/env python3

class LoggedMappingMixin:
    """Add logging to get/set/delete operations for debugging."""
    __slots__ = ()

    def __getitem__(self, key):
        print(f"Getting {str(key)}")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print(f"Setting {key} = {value!r}")
        return super().__setitem__(key, value)
    
    def __delitem__(self, key):
        print(f"Deleting {str(key)}")
        return super().__delitem__(key)
    

class SetOnceMappingMixin:
    """Only allow a key to be set once."""
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"{str(key)} already set")
        return super().__setitem__(key, value)
    

class StringKeysMappingMixin:
    """Restrict keys to strings only."""
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("keys must be strings")
        return super().__setitem__(key, value)


def main():
    """Main entry."""
    print("-*----------------------*-")
    print("-*- LoggedDict Example -*-")
    print("-*----------------------*-")

    class LoggedDict(LoggedMappingMixin, dict):
        pass

    dct = LoggedDict()
    dct["x"] = 23
    print(dct["x"])
    del dct["x"]

    print("-*------------------------------*-")
    print("-*- SetOnceDefaultDict Example -*-")
    print("-*------------------------------*-")
    from collections import defaultdict

    class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
        pass

    dct = SetOnceDefaultDict(list)
    dct["x"].append(2)
    dct["y"].append(3)
    dct["z"].append(10)
    try:
        dct["x"] = 23
    except KeyError as err:
        print(err)


if __name__ == "__main__":
    main()

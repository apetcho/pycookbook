#!/usr/bin/env python3

class RestrictKeysMixin:
    def __init__(self, *args, rkeytype, **kwargs):
        self.__rkeytype = rkeytype
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, self.__rkeytype):
            raise TypeError(f"Keys must be {str(self.__rkeytype)}")
        super().__setitem__(key, value)


class RDict(RestrictKeysMixin, dict):
    pass


def main():
    """Main entry."""
    d = RDict(rkeytype=str)
    e = RDict([("name", "Dave"), ("n", 37)], rkeytype=str)
    f = RDict(name="Dave", n=37, rkeytype=str)
    print(f)
    try:
        f[42] = 10
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    main()

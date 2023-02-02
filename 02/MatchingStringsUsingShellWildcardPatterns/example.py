#!/usr/bin/env python3
"""Example of using shell-wildcard style matching in list comprehensions."""
from fnmatch import fnmatchcase as fmatch


def main():
    """Main entry."""
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    # -*-
    a = [addr for addr in addresses if fmatch(addr, "* ST")]
    print(a)
    # -*-
    b = [addr for addr in addresses if fmatch(addr, "54[0-9][0-9] *CLARK*")]
    print(b)


if __name__ == "__main__":
    main()

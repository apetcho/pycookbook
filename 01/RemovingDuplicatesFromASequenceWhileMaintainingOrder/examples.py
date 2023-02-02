#!/usr/bin/env python3
"""Remove duplicates entries from a sequence while keeping order."""


from typing import Sequence


def dedup1(items:Sequence):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedup2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def main():
    """Main entry."""
    items = [1, 5, 2, 1, 9, 1, 5, 10]
    print(items)
    print(list(dedup1(items)))
    # -*-
    data = [
        dict(x=2, y=3),
        dict(x=1, y=4),
        dict(x=2, y=3),
        dict(x=2, y=3),
        dict(x=10, y=15),
    ]
    print()
    print(data)
    print(list(dedup2(data, key=(lambda d: (d["x"], d["y"])))))
    

if __name__ == "__main__":
    main()

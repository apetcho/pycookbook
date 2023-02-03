#!/usr/bin/env python3
import collections
from collections.abc import Sequence
import bisect


class SortedItems(Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)
    
    def add(self, item):
        bisect.insort(self._items, item)


def main():
    """Main entry."""
    items = SortedItems([5, 1, 3])
    print(list(items))
    print(items[0])
    print(items[-1])
    items.add(2)
    print(list(items))
    items.add(-10)
    print(list(items))
    print(items[1:4])
    print(3 in items)
    print(len(items))
    for n in items:
        print(n)


if __name__ == "__main__":
    main()

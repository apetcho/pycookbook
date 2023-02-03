#!/usr/bin/env python3
from collections.abc import Sequence, MutableSequence
import bisect


class Items(MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, index):
        print(f"Getting: {index}")
        return self._items[index]
    
    def __setitem__(self, index, value):
        print(f"Setting: {index}, {value}")
        self._items[index] = value

    def __delitem__(self, index):
        print(f"Deleting: {index}")
        del self._items[index]

    def insert(self, index, value) -> None:
        print(f"Inserting: {index}, {value}")
        self._items.insert(index, value)

    def __len__(self):
        print("Len")
        return len(self._items)


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
    print("-*---------------*-")
    print("-*- SortedItems -*-")
    print("-*---------------*-")
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

    print("-*-------------------*-")
    print("-*- Items container -*-")
    print("-*-------------------*-")
    items = Items([1, 2, 3])
    print(len(items))
    items.append(4)
    items.append(2)
    print(items.count(2))
    items.remove(3)

if __name__ == "__main__":
    main()

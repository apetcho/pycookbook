#!/usr/bin/env python3

class ListLike:
    def __init__(self):
        self._items = []

    def __getattr__(self, name):
        return getattr(self._items, name)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]


def main():
    """Main entry."""
    a = ListLike()
    a.append(2)
    a.insert(0, 1)
    a.sort()
    print(len(a))
    print(a[0])


if __name__ == "__main__":
    main()

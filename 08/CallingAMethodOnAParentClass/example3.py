#!/usr/bin/env python3

from typing import Any


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        # -*- Delegate attribute lookup to internal obj -*-
        return getattr(self._obj, name)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            # -*- Call original __setattr__
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)


def main():
    """Main entry."""
    class A:
        def __init__(self, x):
            self.x = x

        def spam(self):
            print("A.spam")

    a = A(42)
    proxy = Proxy(a)
    print(proxy.x)
    print(proxy.spam())
    proxy.x = 37
    print(f"Should be 37: {proxy.x}")
    print(f"Should be 37: {a.x}")


if __name__ == "__main__":
    main()

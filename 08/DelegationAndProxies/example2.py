#!/usr/bin/env python3
# A proxy class that wraps around another object, but exposes its public 
# attributes

from typing import Any


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name):
        """Delegate attribute lookup to internal obj."""
        print(f"getattr: {name}")
        return getattr(self._obj, name)
    
    def __setattr__(self, name:str, value:Any):
        """Delegate attribute assignment."""
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            print(f"setattr: ({name}, {value})")
            setattr(self._obj, name, value)

    def __delattr__(self, name:str):
        """Delegate attribute deletion."""
        if name.startswith("_"):
            super().__delattr__(name)
        else:
            print(f"delattr: {name}")
            delattr(self._obj, name)


def main():
    """Main entry."""
    class Spam:
        def __init__(self, x):
            self.x = x

        def bar(self, y):
            print(f"Spam.bar: ({self.x}, {y})")

    # -*- Create an instance -*-
    spam = Spam(2)
    # -*- Create aproxy around it -*-
    proxy = Proxy(spam)
    # -*- Access the proxy -*-
    print(proxy.x)
    spam.bar(3)
    proxy.x = 37


if __name__ == "__main__":
    main()

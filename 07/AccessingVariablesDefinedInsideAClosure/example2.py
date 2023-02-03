#!/usr/bin/env python3
"""Example of faking classes with a closure."""
import sys


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # -*- Update instance dictionary with callables -*-
        self.__dict__.update(
            (key, value) for key, value in locals.items() if callable(value))
        
    def __len__(self) -> int:
        # -+- Redirect special methods
        return self.__dict__["__len__"]()


def stack():
    # -*- Example use -*-
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()
    
    def __len__():
        return len(items)
    
    return ClosureInstance()


def main():
    """Main entry."""
    stk = stack()
    print(stk)
    stk.push(10)
    stk.push(20)
    stk.push("Hello")
    print(len(stk))
    print(stk.pop())
    print(stk.pop())
    print(stk.pop())


if __name__ == "__main__":
    main()

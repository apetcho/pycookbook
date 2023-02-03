#!/usr/bin/env python3
"""Example of a normal class."""


class Stack:
    """Example of Stack class."""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)
    
stk = None

def main():
    """Main entry."""
    global stk
    import example2
    from timeit import timeit

    print("Using a class")
    stk = Stack()
    print(f"{timeit('stk.push(1); stk.pop()', 'from __main__ import stk')}")

    print("Using a closure")
    stk = example2.stack()
    print(f"{timeit('stk.push(1); stk.pop()', 'from __main__ import stk')}")


if __name__ == "__main__":
    main()

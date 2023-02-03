#!/usr/bin/env python3

class A:
    def spam(self, x):
        print("A.spam")

    def foo(self):
        print("A.foo")


class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        print("B.bar")

    def __getattr__(self, name):
        # Expose all of the methods defined on class A.
        return getattr(self._a, name)


def main():
    """Main entry."""
    b = B()
    b.bar()
    b.spam(42)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Tricky initialization problem involving multiple inheritance.
# Does NOT use super()


class Base:
    def __init__(self):
        print("Base.__init__")


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print("A.__init__")


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print("B.__init__")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C.__init__")


def main():
    """Main entry."""
    # -*- Please observe double call of Base.__init__
    _ = C()


if __name__ == "__main__":
    main()

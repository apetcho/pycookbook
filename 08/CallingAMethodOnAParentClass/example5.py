#!/usr/bin/env python3
# Tricky initialization problem involving multiple inheritance.
# Uses super()

class Base:
    def __init__(self):
        print("Base.__init__")


class A(Base):
    def __init__(self):
        super().__init__()
        print("A.__init__")


class B(Base):
    def __init__(self):
        super().__init__()
        print("B.__init__")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("C.__init__")


def main():
    """Main entry."""
    # -*- Observe that each class initialized only once.
    _ = C()


if __name__ == "__main__":
    main()

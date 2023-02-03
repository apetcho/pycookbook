#!/usr/bin/env python3

class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1


def main():
    b = B()
    print(b.x, b.y)


if __name__ == "__main__":
    main()

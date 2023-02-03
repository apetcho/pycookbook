#!/usr/bin/env python3
# Example of using __ method name to implement a non-overrideable method


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print(f"B.__private_method {self.__private}")

    def public_method(self):
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        print("C.__private_method")


def main():
    """Main entry."""
    c = C()
    c.public_method()


if __name__ == "__main__":
    main()

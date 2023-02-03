#!/usr/bin/env python3

class A:
    def spam(self):
        print("A.spam")


class B(A):
    def spam(self):
        print("B.spam")
        super().spam()  # -*- Call parent spam() -*-


def main():
    """Main entry."""
    b = B()
    b.spam()


if __name__ == "__main__":
    main()

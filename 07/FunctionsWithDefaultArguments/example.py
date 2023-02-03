#!/usr/bin/env python3
# Examples of a function with default arguments

from typing import List, Optional


def spam(b=[]):
    # -*- (a) Dangers of using a mutable default argument -*-
    return b


def better_spam(b:Optional[List]=None):
    if b is None:
        b = []
    return b


def main():
    """Main entry."""
    a = spam()
    print(a)
    a.append(1)
    a.append(2)
    b = spam()
    print(b)        # -*- Carfully observe result
    print('-'*10)
    # -*-
    a = better_spam()
    print(a)
    a.append(1)
    a.append(2)
    b = better_spam()
    print(b)
    print('-'*10)


if __name__ == "__main__":
    main()

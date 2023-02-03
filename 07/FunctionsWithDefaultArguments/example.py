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


_no_value = object()

def test_spam(b=_no_value):
    if b is _no_value:
        print("No b value supplied")
    else:
        print(f"b={b}")


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
    # -*- (c) Example of testing if an argument was supplied or not -*-
    test_spam()
    test_spam(None)
    test_spam(0)
    test_spam([])



if __name__ == "__main__":
    main()

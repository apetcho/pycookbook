#!/usr/bin/env python3
"""Example of accessing variables inside a closure."""


def sample():
    n = 0

    def fun():
        # -*- Closure function -*-
        print(f"n = {n}")

    def get_n():
        # -*- Accessor methods for n -*-
        return n
    
    def set_n(value):
        nonlocal n
        n = value

    # -*- Attach as function attributes -*-
    fun.get_n = get_n
    fun.set_n = set_n
    return fun


def main():
    fn = sample()
    fn()
    n = 0
    fn.set_n(10)
    fn()
    print(fn.get_n())

    
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# This example is about the problem of carrying extra state around callback 
# functions. To test the examples, this very simple code emulates the typical
# control of a callback.

from typing import Any, Callable, Sequence


def apply_async(fun:Callable, args:Sequence, *, callback:Callable) -> None:
    # -*- Compute the result
    result = fun(*args)
    # -*- Invoke the callback with the result
    callback(result)


def add(x, y):
    """A simplex function for testing."""
    return x + y


def print_result(result:Any) -> None:
    print(f"Got: {result}")


def main():
    # -*- (a) A simple callback example -*-
    print("-*------------------*-")
    print("-*- Simple Example -*-")
    print("-*------------------*-")
    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, ("hello", "world"), callback=print_result)


if __name__ == "__main__":
    main()

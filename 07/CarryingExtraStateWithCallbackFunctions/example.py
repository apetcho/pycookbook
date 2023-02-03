#!/usr/bin/env python3
# This example is about the problem of carrying extra state around callback 
# functions. To test the examples, this very simple code emulates the typical
# control of a callback.

from typing import Any, Callable, Sequence
from functools import partial


def apply_async(fun:Callable, args:Sequence, *, callback:Callable) -> None:
    # -*- Compute the result
    result = fun(*args)
    # -*- Invoke the callback with the result
    callback(result)


def add(x, y):
    """A simplex function for testing."""
    return x + y


def print_result(result:Any) -> None:
    print(f"Result: {result}")


class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print(f"[{self.sequence}] Result: {result}")


def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f"[{sequence}] Result: {result}")

    return handler


def make_coroutine():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print(f"[{sequence}] Result: {result}")


class SequenceNo:
    def __init__(self):
        self.sequence = 0


def seq_handler(result, seq:SequenceNo):
    seq.sequence += 1
    print(f"[{seq.sequence}] Result: {result}")


def main():
    # -*- (a) A simple callback example -*-
    print("-*------------------*-")
    print("-*- Simple Example -*-")
    print("-*------------------*-")
    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, ("hello", " simple example"), callback=print_result)
    print("-*--------------------------*-")
    print("-*- Using a bounded-method -*-")
    print("-*--------------------------*-")
    result = ResultHandler()
    apply_async(add, (2, 3), callback=result.handler)
    apply_async(add, ("hello", " bounded-metho"), callback=result.handler)
    # -*- (c) Using a closure
    print("-*-------------------*-")
    print("-*- Using a closure -*-")
    print("-*-------------------*-")
    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ("hello", " closure"), callback=handler)
    # -*- (d) Using a coroutine
    print("-*---------------------*-")
    print("-*- Using a coroutine -*-")
    print("-*---------------------*-")
    coro = make_coroutine()
    next(coro)
    apply_async(add, (2, 3), callback=coro.send)
    apply_async(add, ("hello", " coroutine"), callback=coro.send)
    # -*- (e) Partial function application -*-
    print("-*--------------------------------------*-")
    print("-*- Using partial function application -*-")
    print("-*--------------------------------------*-")
    seq = SequenceNo()
    apply_async(add, (2, 3), callback=partial(seq_handler, seq=seq))
    apply_async(
        add, ("hello", " partial function application"),
        callback=partial(seq_handler, seq=seq)
    )


if __name__ == "__main__":
    main()

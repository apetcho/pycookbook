#!/usr/bin/env python3
# Example of implementing an inlined-callback function
import multiprocessing
from queue import Queue
from functools import wraps
from typing import Collection



def apply_async(fun, args:Collection, *, callback) -> None:
    """Sample function to illustrate callback control flow."""
    # -*- Compute the result.
    result = fun(*args)
    # -*- Invoke the callpback with the result
    callback(result)


class Async:
    def __init__(self, fun, args):
        self.fun = fun
        self.args = args

def inlined_async(fun):
    @wraps(fun)
    def wrapper(*args):
        fn = fun(*args)
        resultQ = Queue()
        resultQ.put(None)
        while True:
            result = resultQ.get()
            try:
                a = fn.send(result)
                apply_async(a.fun, a.args, callback=resultQ.put)
            except StopIteration:
                break
    return wrapper

def add(x, y):
    # -*- Sample use -*-
    return x + y


@inlined_async
def test():
    res = yield Async(add, (2, 3))
    print(res)
    res = yield Async(add, ("Hello", " world"))
    print(res)
    for n in range(10):
        res = yield Async(add, (n, n))
        print(res)
    print("Goodbye")


def main():
    """Main entry."""
    # -*- Simple test -*-
    print("-*---------------*-")
    print("-*- Simple test -*-")
    print("-*---------------*-")
    test()

    print("-*------------------------*-")
    print("-*- Multiprocessing test -*-")
    print("-*------------------------*-")
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async
    test()


if __name__ == "__main__":
    main()

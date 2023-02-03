#!/usr/bin/env python3
# Examples of keyword-only argument functions

def recv(maxsize, *, block=True):
    """A simple keyword-only argument"""
    print(maxsize, block)


def minimum(*values, clip=None):
    """Adding keyword-only args to *args functions."""
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


def main():
    """Main entry."""
    recv(8192, block=False)
    try:
        recv(8192, False)
    except TypeError as err:
        print(err)

    print(minimum(1, 5, 2, -5, 10))
    print(minimum(1, 5, 2, -5, 10, clip=0))


if __name__ == "__main__":
    main()

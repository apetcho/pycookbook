#!/usr/bin/env python
"""Unpacking of tagged tuples of varying sizes."""


def main():
    """Main entry."""
    records = [
        ("foo", 1, 2),
        ("bar", "hello"),
        ("foo", 3, 4),
    ]

    funs = {
        "foo": (lambda x, y: print(f"foo {x} {y}")),
        "bar": (lambda s: print(f"bar {s}")),
    }

    for tag, *args in records:
        if tag == "foo":
            funs["foo"](*args)
        elif tag == "bar":
            funs["bar"](*args)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Example of combining text via generators."""
import sys

def sample():
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield "".join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


def main():
    """Main entry."""
    # -*- (a) Simple join operator -*-
    text = "".join(sample())
    print(text)

    # -*- (b) Redirection of parts to I/O -*-
    for part in sample():
        sys.stdout.write(part)
    sys.stdout.write("\n")

    # -*- (c) Combination of parts into buffers and larger I/O operations -*-
    for part in combine(sample(), 32768):
        sys.stdout.write(part)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

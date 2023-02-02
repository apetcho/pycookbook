#!/usr/bin/env python3
"""Example of splitting a string on multiple delimiters using a regex."""
import re


def main():
    """Main entry."""
    line = "asdf fjdk; afed, fjek,asdf,        foo"
    # -*- (a) Splitting on space, comma, and semicolon -*-
    parts = re.split(r"[;,\s]\s*", line)
    print(parts)
    # -*- (b) Splitting with a capture group -*-
    fields = re.split(r"(;|,|\s)\s*", line)
    print(fields)
    # -*- (c) Rebuilding a string using fields above -*-
    values = fields[::2]
    delimiters = fields[1::2]
    delimiters.append("")
    print(f"value = {values}")
    print(f"delimiters = {delimiters}")
    newline = "".join(v+d for v,d in zip(values, delimiters))
    print(f"newline = {newline}")
    # -*- (d) Splitting using a non-capture group -*-
    parts = re.split(r"(?:,|;|\s)\s*", line)
    print(parts)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Example of a tokenizer."""
import re
from collections import namedtuple

Token = namedtuple("Token", ["type", "value"])

def generate_tokens(pat:re.Match, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


def main():
    """Main entry."""
    NAME = r"(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)"
    NUM = r"(?P<NUM>\d+)"
    PLUS = r"(?P<PLUS>\+)"
    TIMES = r"(?P<TIMES>\*)"
    EQ = r"(?P<EQ>=)"
    WS = r"(?P<WS>\s+)"

    master_pat = re.compile("|".join([NAME, NUM, PLUS, TIMES, EQ, WS]))
    for token in generate_tokens(master_pat, "foo = 43"):
        print(token)



if __name__ == "__main__":
    main()

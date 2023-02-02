#!/usr/bin/env python3
"""Example of a regular expression that finds shortest matches."""
import re


def main():
    """Main entry."""
    # -*- Sample text -*-
    text = "Computer says 'no.' Phone says 'yes.'"
    # -*- (a) Regex that finds quoted strings - longest match -*-
    strpat = re.compile(r"\'(.*)\'")
    print(strpat.findall(text))
    # -*- (b) Regex that finds quoted strings - shortest match -*-
    strpat = re.compile(r"\'(.*?)\'")
    print(strpat.findall(text))


if __name__ == "__main__":
    main()

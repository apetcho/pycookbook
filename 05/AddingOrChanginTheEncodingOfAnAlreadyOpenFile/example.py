#!/usr/bin/env python3
"""Example of adding a text encoding to existing file-like object."""
from urllib.request import urlopen
from io import TextIOWrapper


def main():
    """Main entry."""
    urlobj = urlopen("http://www.python.org")
    fp = TextIOWrapper(urlobj, encoding="utf-8")
    text = fp.read()
    print(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Some examples of reading text file with different options.

The file sample.tyt is a UTF-8 encoded text file with Windows line-endings 
(\r\n).
"""



def main():
    """Main entry."""
    import os
    filename = os.path.join(os.path.dirname(__file__), "sample.txt")
    # -*- (a) Reading a basic text file (UTF-8 default encoding)
    print("Reading a simple text file (UTF-8)")
    with open(filename, "rt") as fp:
        for line in fp:
            print(repr(line))

    # -*- (b) Reading a text file with universal newlines turned off
    print()
    print("Reading text file with universal newlines off")
    with open(filename, "rt", newline="") as fp:
        for line in fp:
            print(repr(line))

    # -*- (c) Reading text file as ASCII with replacement error handling
    print()
    print("Reading text as ASCII with replacement error handling")
    with open(filename, "rt", encoding="ascii", errors="replace") as fp:
        for line in fp:
            print(repr(line))

    # -*- (d) Reading text file as ASCII with ignore error handling
    print()
    print("Reading text as ASCII with ignore error handling")
    with open(filename, "rt", encoding="ascii", errors="ignore") as fp:
        for line in fp:
            print(repr(line))


if __name__ == "__main__":
    main()

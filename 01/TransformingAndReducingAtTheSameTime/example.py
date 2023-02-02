#!/usr/bin/env python3
"""Some examples of using generators in arguments."""
import os


def main():
    """Main entry."""
    files = os.listdir(os.path.expanduser("~"))
    if any(name.endswith(".py") for name in files):
        print("There be python!")
    else:
        print("Sorry, no python.")

    # -*- Output a tuple as CSV -*-
    s = ("ACME", 50, 123.45)
    print(",".join(str(x) for x in s))

    # -*- Data reduction across fields of a data structure -*-
    portfolio = [
        {"name": "GOOG", "shares": 50},
        {"name": "YHOO", "shares": 75},
        {"name": "AOL", "shares": 20},
        {"name": "SCOX", "shares": 65},
    ]
    minshares = min(stock["shares"] for stock in portfolio)
    print(minshares)


if __name__ == "__main__":
    main()

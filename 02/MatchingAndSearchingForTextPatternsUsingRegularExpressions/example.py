#!/usr/bin/env python3
"""Examples of simple regular expression matching"""
import re


def main():
    """Main entry."""
    # -*- Some sample text -*-
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."

    # -*- (a) Find all matching dates -*-
    datepat = re.compile(r"\d+/\d+/\d+")
    print(f"{datepat.findall(text)}")

    # -*- (b) Find all matching dates with capture groups -*-
    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    for month, day, year in datepat.findall(text):
        print(f"{year}-{month}-{day}")

    # -*- (c) Iterative search -*-
    for match in datepat.finditer(text):
        print(f"{match.groups()}")


if __name__ == "__main__":
    main()

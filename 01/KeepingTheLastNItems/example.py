#!/usr/bin/env python3
"""Keeing the last n items."""
from collections import deque
from typing import List


def search(lines:List[str], pattern:str, history:int=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def main():
    """Main entry."""
    import os
    filename = os.path.join(os.path.dirname(__file__), "somefile.txt")
    with open(filename) as fp:
        for line, prevlines in search(fp, "python", 3):
            for k, pline in enumerate(prevlines):
                print(f"[{(k+1):02}] {pline}", end="")
            print(line, end="")
            print('-'*20)


if __name__ == "__main__":
    main()


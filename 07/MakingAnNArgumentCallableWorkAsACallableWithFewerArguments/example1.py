#!/usr/bin/env python3
# -*- Example of using partial() with sorting a list of (x, y) coordinates
import functools
import math
from typing import Tuple


def distance(p1:Tuple[float, float], p2:Tuple[float, float]) -> float:
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)


def main():
    """Main entry."""
    points = [(1, 2), (3, 4), (5, 6), (7, 7)]
    point = (4, 3)
    points.sort(key=functools.partial(distance, point))
    print(points)


if __name__ == "__main__":
    main()

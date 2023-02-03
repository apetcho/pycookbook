#!/usr/bin/env python3
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x!r}, {self.y!r})"
    
    def distance(self, x, y):
        return math.hypot(self.x-x, self.y-y)


def main():
    """Main entry."""
    point = Point(2, 3)
    print("-*-------------------------*-")
    print("-*- Method 1: Use getattr -*-")
    print("-*-------------------------*-")
    dist = getattr(point, "distance")(0, 0)
    print(f"distance = {dist}")


if __name__ == "__main__":
    main()

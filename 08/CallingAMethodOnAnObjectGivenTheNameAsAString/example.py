#!/usr/bin/env python3
import math
import operator


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
    print("-*------------------------------*-")
    print("-*- Method 2: Use methodcaller -*-")
    print("-*------------------------------*-")
    dist = operator.methodcaller("distance", 0, 0)(point)
    print(f"distance = {dist}")
    print("-*--------------------------*-")
    print("-*- Application in sorting -*-")
    print("-*--------------------------*-")
    points = [
        Point(1, 2), Point(3, 0), Point(10, -3),
        Point(-5, -7), Point(-1, 8), Point(3, 2)
    ]
    # -*- Sort by distance from origin (0, 0) -*-
    points.sort(key=operator.methodcaller("distance", 0, 0))
    for point in points:
        print(point)

if __name__ == "__main__":
    main()

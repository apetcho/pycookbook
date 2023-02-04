#!/usr/bin/env python3
import math

class Structure:
    """Structure class."""
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments.")
        
        # -*-
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# -*-
class Stock(Structure):
    _fields = ["name", "shares", "price"]

    def __repr__(self) -> str:
        return (
            f"Stock(name={self.name}, shares={self.shares}, "
            f"price={self.price})"
        ) 

class Point(Structure):
    _fields = ["x", "y"]

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

class Circle(Structure):
    _fields = ["radius"]

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"

    def area(self) -> float:
        return math.pi * self.radius ** 2


def main():
    """Main entry."""
    stock = Stock("ACME", 50, 91.1)
    print(stock)
    point = Point(2, 3)
    print(point)
    circle = Circle(4.5)
    print(circle)

    try:
        stock2 = Stock("ACME", 50)
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    main()

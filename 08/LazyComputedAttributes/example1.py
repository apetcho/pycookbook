#!/usr/bin/env python3

from typing import Callable


class LazyProperty:
    def __init__(self, fun:Callable):
        self.fun = fun

    def __get__(self, instance, cls):
        if instance is None:
            return self
        value = self.fun(instance)
        setattr(instance, self.fun.__name__, value)
        return value
    

def main():
    """Main entry."""
    import math
    import random

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @LazyProperty
        def area(self):
            print("Computing area")
            return math.pi * self.radius ** 2
        
        @LazyProperty
        def perimeter(self):
            print("Computing perimeter")
            return 2 * math.pi * self.radius
        
        def __repr__(self) -> str:
            return (
                f"Circle(radius={self.radius}), area={self.area}, "
                f"perimeter={self.perimeter}"
            )
        
    for _ in range(10):
        print(Circle(random.randint(2, 10)))
    

if __name__ == "__main__":
    main()

#!/usr/bin/env python3


from typing import Callable


def lazyproperty(fun:Callable):
    name = f"_lazy_{fun.__name__}"
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        value = fun(self)
        setattr(self, name, value)
        return value
    return lazy


def main():
    """Main entry."""
    import math
    import random

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        @lazyproperty
        def area(self):
            print("Computing area")
            return math.pi * self.radius ** 2
        
        @lazyproperty
        def perimeter(self):
            print("Computing perimeter")
            return 2 * math.pi * self.radius
        
        def __repr__(self) -> str:
            return (
                f"Circle(radius={self.radius}), "
                f"area={self.area}, perimeter={self.perimeter}"
            )
    
    for _ in range(5):
        print(Circle(random.randint(3, 12)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# Descriptor for a type-checked attribute

class Typed:
    def __init__(self, name, expectedType):
        self.name = name
        self.expectedType = expectedType

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expectedType):
            raise TypeError(f"Expected {str(self.expectedType)}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    """Class decorator that applies it to selected attributes."""
    def decorate(cls):
        for name, expectedType in kwargs.items():
            # Attach a Typed descriptor to the class.
            setattr(cls, name, Typed(name, expectedType))
        return cls
    return decorate


# -*---------------*-
# -*- Example use -*-
# -*---------------*-
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


def main():
    """Main entry."""
    stock = Stock("ACME", 100, 490.1)
    print(stock.name, stock.shares, stock.price)
    try:
        stock.shares = "a lot"
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    main()

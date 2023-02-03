#!/usr/bin/env python3
# -*- Base class. Uses a descriptor to set a value -*-

class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        self.__dict__.update(opts)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    """Descriptor for enforcing types."""
    expectedType = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expectedType):
            raise TypeError(f"expected {str(self.expectedType)}")
        super().__set__(instance, value)


class Unsigned(Descriptor):
    """Descriptor for enforcing values."""

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Expected >= 0")
        super().__set__(instance, value)


class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if "size" not in opts:
            raise TypeError("missing size option")
        self.size = opts["size"]
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError(f"size must be < {str(self.size)}")
        super().__set__(instance, value)


class Integer(Typed):
    expectedType = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expectedType = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expectedType = str


class SizedString(String, MaxSized):
    pass


def check_attributes(**kwargs):
    """Class decorator to apply constraints"""
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate



class ChecedMeta(type):
    """A metaclass that applies checking."""

    def __new__(cls, clsname, bases, methods):
        # -*- Attach attribute names to the descriptors
        for key, value in methods.items():
            value.name = key
        return type.__new__(cls, clsname, bases, methods)


def test(s):
    # -*- Tesing code -*-
    print(s.name)
    s.shares = 75
    print(s.shares)
    try:
        s.shares = -10
    except ValueError as err:
        print(err)

    try:
        s.price = "a lot"
    except TypeError as err:
        print(err)

    try:
        s.name = "ABRACADABRA"
    except ValueError as err:
        print(err)


def main():
    """Main entry."""
    print("-*--------------------------*-")
    print("-*- Class with descriptors -*-")
    print("-*--------------------------*-")

    class Stock(ChecedMeta):
        # -*- Specify constrains -*-
        name = SizedString("name", size=8)
        shares = UnsignedInteger("shares")
        price = UnsignedFloat("price")

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    stock = Stock("ACME", 50, 91.1)
    test(stock)

    print("-*------------------------*-")
    print("-*- Class with metaclass -*-")
    print("-*------------------------*-")
    class Stock(ChecedMeta):
        name = SizedString(size=8)
        shares = UnsignedInteger()
        price = UnsignedFloat()

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    stock = Stock("ACME", 50, 91.1)
    test(stock)


if __name__ == "__main__":
    main()

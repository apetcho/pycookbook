#!/usr/bin/env python3

class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")
        # -*- Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # -*- Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        # -*- Check any remaining unknown arguments
        if kwargs:
            raise TypeError(f"Invalid arguments(s): {','.join(kwargs)}")


class Stock(Structure):
    _fields = ["name", "shares", "price"]

    def __repr__(self) -> str:
        return (
            f"Stock(name={self.name}, shares={self.shares}, "
            f"price={self.price})"
        )


def main():
    """Main entry."""
    stock1 = Stock("ACME", 50, 91.1)
    stock2 = Stock("ACME", 50, price=91.1)
    stock3 = Stock("ACME", shares=50, price=91.1)
    for stock in (stock1, stock2, stock3):
        print(stock)


if __name__ == "__main__":
    main()

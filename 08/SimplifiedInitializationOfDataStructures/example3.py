#!/usr/bin/env python3

class Structure:
    _fields = []
    #_extran = {}

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")
        
        # -*-
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # -*- Additional arguments (if any)
        extraArgs = kwargs.keys() - self._fields
        self._extra = {}
        for name in extraArgs:
            val = kwargs.pop(name)
            setattr(self, name, val)
            if name not in self._fields:
                self._extra[name] = val
        setattr(self, "_extra_", self._extra.copy())

        if kwargs:
            raise TypeError(f"Duplication values for {','.join(kwargs)}")


class Stock(Structure):
    _fields = ["name", "shares", "price"]

    def __repr__(self) -> str:
        extra = "{}"
        if len(self._extra) > 0:
            extra = f"{self._extra!r}"
            return (
                f"Stock(name={self.name}, shares={self.shares}, "
                f"price={self.price}, extra={extra})"
            )
        else:
            return (
                f"Stock(name={self.name}, shares={self.shares}, "
                f"price={self.price})"
            )
        

def main():
    """Main entry."""
    stock1 = Stock("ACME", 50, 91.1)
    stock2 = Stock("ACME", 50, 91.1, date="8/12/2022")
    for stock in (stock1, stock2):
        print(stock)


if __name__ == "__main__":
    main()

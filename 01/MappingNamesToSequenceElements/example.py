#!/usr/bin/env python3
from collections import namedtuple

Stock = namedtuple("Stock", ["name", "shares", "price"])


def compute_cost(records):
    """Compute cost."""
    total = 0.0
    for record in records:
        stock = Stock(*record)
        total += stock.shares * stock.price
    return total


def main():
    """Main entry."""
    records = [
        ("GOOG", 100, 490.1),
        ("ACME", 100, 123.45),
        ("IBM", 50, 91.15),
    ]
    print(compute_cost(records))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Example of using heapq to find the N smallest or largest items."""
import heapq


def main():
    """Main entry"""
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]

    cheap = heapq.nsmallest(3, portfolio, key=(lambda stock: stock["price"]))
    expensive = heapq.nlargest(3, portfolio, key=(lambda stock: stock["price"]))
    print(cheap)
    print(expensive)


if __name__ == "__main__":
    main()

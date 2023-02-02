#!/usr/bin/env python3

prices = {
    "ACME": 45.23,
    "AAPL": 612.78,
    "IBM": 205.55,
    "HPQ": 37.20,
    "FB": 10.75,
}

def main():
    # -*- Find min and max price -*-
    minprice = min(zip(prices.values(), prices.keys()))
    maxprice = max(zip(prices.values(), prices.keys()))
    print(f"min price: {minprice}")
    print(f"max price: {maxprice}")

    print("Sorted prices:")
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    for price, name in prices_sorted:
        print(f"    {name} {price}")


if __name__ == "__main__":
    main()

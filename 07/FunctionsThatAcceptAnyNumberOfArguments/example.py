#!/usr/bin/env python3
# -*- Example of *args and **kwargs functions -*-

def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))


def main():
    """Main entry."""
    print(avg(1, 2))
    print(avg(1, 2, 3, 4, 5))


if __name__ == "__main__":
    main()

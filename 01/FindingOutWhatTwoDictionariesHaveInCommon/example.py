#!/usr/bin/env python3
"""Find out what two dictionaries have in common"""

def main():
    """Main entry."""
    a = dict(x=1, y=2, z=3)
    b = dict(w=10, x=11, y=2)
    print(f"Common keys: {a.keys() & b.keys()}")
    print(f"Keys in a not in b: {a.keys() - b.keys()}")
    print(f"(key, value) pairs in common: {a.items() & b.items()}")


if __name__ == "__main__":
    main()

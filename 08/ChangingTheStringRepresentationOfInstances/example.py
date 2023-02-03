#!/usr/bin/env python3

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Pair({self.x!r}, {self.y!r})"
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    

def main():
    """Main entry."""
    import random
    import time
    random.seed(time.time())
    k = 0
    for _ in range(10):
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        pair = Pair(x, y)
        print(f"[{(k+1):02d}] {str(pair)} <==> {repr(pair)}")
        k += 1


if __name__ == "__main__":
    main()

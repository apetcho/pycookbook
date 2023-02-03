#!/usr/bin/env python3

_Formats = {
    "ymd": "{d.year}-{d.month}-{d.day}",
    "mdy": "{d.month}/{d.day}/{d.year}",
    "dmy": "{d.day}/{d.month}/{d.year}",
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, fmt):
        if fmt == "":
            fmt = "ymd"
        _format = _Formats[fmt]
        return _format.format(d=self)
    

def main():
    """Main entry."""
    import random
    for _ in range(10):
        year = random.randint(2000, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 30)
        print(f"{Date(year, month, day)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        date = cls.__new__(cls)
        _time = localtime()
        date.year = _time.tm_year
        date.month = _time.tm_mon
        date.day = _time.tm_mday
        return date


def main():
    """Main entry."""
    date = Date.__new__(Date)
    print(date)
    print(hasattr(date, "year"))
    data = {"year": 2023, "month": 1, "day": 12}
    date.__dict__.update(data)
    print(date.year)
    print(date.month)
    date = Date.today()
    print(date.year, date.month, date.day)




if __name__ == "__main__":
    main()

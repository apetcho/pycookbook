#!/usr/bin/env python3
import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        _time = time.localtime()
        return cls(_time.tm_year, _time.tm_mon, _time.tm_mday)
    

def main():
    """Main entry"""
    a = Date(2012, 12, 21)
    b = Date.today()
    print(a.year, a.month, a.day)
    print(b.year, b.month, b.day)


    class NewDate(Date):
        pass

    c = Date.today()
    d = NewDate.today()
    print(f"Should be Date instance: {Date}")
    print(f"Should be NewDate instance: {NewDate}")


if __name__ == "__main__":
    main()

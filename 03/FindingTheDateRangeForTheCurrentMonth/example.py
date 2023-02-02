#!/usr/bin/env python3
from datetime import datetime, date, timedelta
import calendar
from typing import Tuple


def get_month_range(start_date=None) -> Tuple[date, date]:
    if start_date is None:
        start_date = date.today().replace(day=1)
    days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def main():
    """Main entry."""
    first_day, last_day = get_month_range()
    a_day = timedelta(days=1)
    while first_day < last_day:
        print(f">>> {first_day}")
        first_day += a_day
    # -*-
    print()
    for d in date_range(date(2012, 8, 1), date(2012, 8, 11), timedelta(days=1)):
        print(f"=> {d}")
    print()
    start = date(2012, 8, 1)
    stop = date(2012, 8, 3)
    step = timedelta(hours=12)
    for day in date_range(start, stop, step):
        print(f" -> {day}")


if __name__ == "__main__":
    main()

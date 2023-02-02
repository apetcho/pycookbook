#!/usr/bin/env python3
"""Group records together based on a field."""
from itertools import groupby
from collections import defaultdict


def main():
    """Main entry."""
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    rows.sort(key=(lambda row: row["date"]))
    for date, items in groupby(rows, key=(lambda row: row["date"])):
        print(date)
        for item in items:
            print(f"    {item}")

    # -*- Example of building a multidict
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row["date"]].append(row)

    for row in rows_by_date["07/01/2012"]:
        print(row)


if __name__ == "__main__":
    main()

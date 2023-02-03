#!/usr/bin/env python3
"""Various ways of reading CSV files."""
import csv
from collections import namedtuple


def _get_filename() -> str:
    import os
    filename = os.path.join(os.path.dirname(__file__), "stocks.csv")
    return filename


def _read_as_tuples():
    print("Reading as tuples:")
    with open(_get_filename()) as fp:
        reader = csv.reader(fp)
        headers = next(reader)
        print(f"    {headers}")
        for row in reader:
            print(f"    {row}")


def _read_as_namedtuples():
    print("\nReading as namedtuples")
    with open(_get_filename()) as fp:
        reader = csv.reader(fp)
        Row = namedtuple("Row", next(reader))
        for line in reader:
            row = Row(*line)
            print(f"    {row}")


def _read_as_dictionaries():
    print("\nReading as dicts")
    with open(_get_filename()) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            print(f"    {row}")


def _read_into_tuple_with_type_conversion():
    print("\nReading into tuples with type conversion")
    coltypes = [str, float, str, str, float, int]
    with open(_get_filename()) as fp:
        reader = csv.reader(fp)
        headers = next(reader)
        for row in reader:
            # -*- Apply conversion to row items
            row = tuple(
                convert(value) for convert, value in zip(coltypes, row)
            )
            print(row)


def _convert_selected_dict_fields():
    print("\nReading as dicts with type conversion")
    fieldtypes = [
        ("Price", float), ("Change", float), ("Volume", int)
    ]
    with open(_get_filename()) as fp:
        for row in csv.DictReader(fp):
            row.update(
                (key, conversion(row[key]))
                for key, conversion in fieldtypes    
            )
            print(row)


def main():
    """Main entry."""
    # -*- (a) Reading as tuples
    _read_as_tuples()
    # -*- (b) Reading as nametuples
    _read_as_namedtuples()
    # -*- (c) Reading as dictionaries
    _read_as_dictionaries()
    # -*- (d) Reading into tuples with type conversion
    _read_into_tuple_with_type_conversion()
    # -*- (e) Converting selected dict fields.
    _convert_selected_dict_fields()


if __name__ == "__main__":
    main()

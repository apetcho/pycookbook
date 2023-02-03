#!/usr/bin/env python3
"""Example of incremental XML parsing"""
# The file 'potholes.xml' is a greatly condensed version of a larger file file
# available for download at
# https://data.cityofchicago.org/api/views/7as2-ds3y/rows.xml?accessType=DOWNLOAD
from xml.etree.ElementTree import iterparse
from collections import Counter


def parse_and_remove(filename:str, path:str):
    path_parts = path.split("/")
    doc = iterparse(filename, ("start", "end"))
    # -*- Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == "start":
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        if event == "end":
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


def main():
    """Main entry."""
    # -*- Find zip code with most potholes -*-
    import os
    filename = os.path.join(os.path.dirname(__file__), "potholes.xml")
    potholes_by_zip = Counter()
    data = parse_and_remove(filename, "row/row")
    for pothole in data:
        potholes_by_zip[pothole.findtext("zip")] += 1

    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, num)
    

if __name__ == "__main__":
    main()

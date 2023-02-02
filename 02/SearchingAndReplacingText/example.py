#!/usr/bin/env python3
"""Examples of simple regular expression substitution."""
import re
from calendar import month_abbr


def change_date(m:re.Match):
    mon_name = month_abbr[int(m.group(1))]
    return f"{m.group(2)} {mon_name} {m.group(3)}"


def main():
    """Main entry."""
    # -*- Some sample text -*-
    text = "Today is 11/27/2012. PyCon starts 3/13/2013."
    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    # -*- (a) Simple substitution -*-
    print(datepat.sub(r"\3-\1-\2", text))
    # -*- (b) Replacement function -*-
    print(datepat.sub(change_date, text))


if __name__ == "__main__":
    main()

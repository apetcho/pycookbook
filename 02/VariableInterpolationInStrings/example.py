#!/usr/bin/env python3
"""Examples of variable interpolation."""
import sys


class SafeSub(dict):
    """Class for performing safe substitutions."""

    def __missing__(self, key):
        return f"{key:s}"
    

def main():
    """Main entry."""
    s = "{name} has {n} messages."

    # -*- (a) Simple substitution -*-
    name, n = "Guido", 37
    print(s.format_map(vars()))

    # -*- (b) Safe substitution with missing values -*-
    del n
    print(s.format_map(SafeSub(vars())))

    # -*- (c) Safe substitution - frame hack -*-
    n = 37
    sub = (
        lambda txt: txt.format_map(SafeSub(sys._getframe(1).f_locals))
    )
    print(sub("Hello {name}"))
    print(sub("{name} has {n} messages"))
    print(sub("Your favorite color is {color}"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Example of combining dicts and chainmap."""
from collections import ChainMap


def main():
    """Main entry."""
    a = dict(x=1, z=3)
    b = dict(y=2, z=4)
    c = ChainMap(a, b)
    print(f"c['x'] = {c['x']}  # Expected Output: 1  (from a)")
    print(f"c['y'] = {c['y']}  # Expected Output: 2  (from b)")
    print(f"c['z'] = {c['z']}  # Expected Output: 3  (from a)")

    # -*- Output some common values -*-
    print(f"len(c): {len(c)}")
    print(f"c.keys(): {list(c.keys())}")
    print(f"c.values(): {list(c.values())}")
    print(f"c: {c}")

    # -*- Modify some values -*-
    c["z"] = 10
    print(f"c: {c}")
    c["w"] = 40
    print(f"c: {c}")
    del c["x"]
    print(f"c: {c}")
    print(f"a: {a}")

    # -*- Example of stacking mappings (like scopes)
    values = ChainMap()
    values["x"] = 1
    print(f"values = {values}")

    # -*- Add a new mapping -*-
    values = values.new_child()
    print(f"values = {values}")
    values["x"] = 2
    print(f"values = {values}")

    # -*- Add a new mapping -*-
    values = values.new_child()
    values["x"] = 3
    print(f"values = {values}")
    print(f"values['x'] = {values['x']}")

    # -*- Discard last mapping -*-
    values = values.parents
    print(f"values = {values}")
    print(f"values['x'] = {values['x']}")

    # -*- Discard last mapping -*-
    values = values.parents
    print(f"values = {values}")
    print(f"values['x'] = {values['x']}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import struct
import itertools


def _get_filepath():
    import os
    return os.path.join(os.path.dirname(__file__), "polys.bin")


def write_polys(filename, polys):
    # -*- Determine bounding box
    flattened = list(itertools.chain(*polys))
    xmin = min(x for x, _ in flattened)
    xmax = max(x for x, _ in flattened)
    ymin = min(y for _, y in flattened)
    ymax = max(y for _, y in flattened)

    with open(filename, "wb") as fp:
        fp.write(
            struct.pack(
                "<iddddi", 0x1234, xmin, ymin, xmax, ymax, len(polys)
            )
        )
        for poly in polys:
            size = len(poly) * struct.calcsize("<dd")
            fp.write(struct.pack("<i", size+4))
            for pt in poly:
                fp.write(struct.pack("<dd", *pt))


def main():
    """Main entry."""
    polys = [
        [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
        [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
        [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
    ]

    # -*- Call it with our polygon data -*-
    write_polys(_get_filepath(), polys)


if __name__ == "__main__":
    main()

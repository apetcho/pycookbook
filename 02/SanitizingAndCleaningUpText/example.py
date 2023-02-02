#!/usr/bin/env python3
"""Example of some tricky sanitization problems."""

import unicodedata
import sys


def main():
    """Main entry."""
    # -*- A tricky string -*-
    s = "p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n"
    print(s)

    # -*- (a) Remappin whitespace -*-
    remap = {
        ord('\t'): " ",
        ord("\f"): " ",
        ord("\r"): None     # Deleted
    }

    a = s.translate(remap)
    print(f"Whitespace remapped: {a}")

    # -*- (b) Remove all combining characters/marks
    cmb_chrs = dict.fromkeys(
        c for c in range(sys.maxunicode) if unicodedata.combining(chr(c))
    )
    b = unicodedata.normalize("NFD", a)
    c = b.translate(cmb_chrs)
    print(f"accents removed: {c}")

    # -*- (c) Accent removal using I/O decoding -*-
    d = b.encode("ascii", "ignore").decode("ascii")
    print(f"accents removed via I/O: {d}")




if __name__ == "__main__":
    main()

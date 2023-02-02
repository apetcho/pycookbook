#!/usr/bin/env python3
"""Example of getting a directory listing"""
import os
import glob


def main():
    """Main entry."""
    path = os.path.join(os.path.dirname(__file__), "*.py")
    pyfiles = glob.glob(path)
    # -*- get file sizes and modification dates -*-
    name_sz_date = [
        (name, os.path.getsize(name), os.path.getmtime(name))
        for name in pyfiles
    ]
    for nsd in name_sz_date:
        print(nsd)

    # -*- get file metadata
    print()
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)


if __name__ == "__main__":
    main()

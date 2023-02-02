#!/usr/bin/env python3
"""Example of writing raw bytes on a file opened in text mode."""
import sys


def main():
    """Main entry."""
    data = b"Hello World\n"
    # -*- Write onto the buffer attribute (bypassing text encoding)
    sys.stdout.buffer.write(data)


if __name__ == "__main__":
    main()

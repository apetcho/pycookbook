#!/usr/bin/env python3
"""Regular expression that matches multiline patterns"""
import re


def main():
    """Main entry."""
    text = """/* this is a
                    mulitline comments */
    """
    comment = re.compile(r"/\*((?:.|\n)*?)\*/")
    print(comment.findall(text))


if __name__ == "__main__":
    main()

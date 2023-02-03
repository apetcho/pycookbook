#!/usr/bin/env python3
"""Example of XML namespace handling."""
from xml.etree.ElementTree import parse


class XMLNamespaces:
    def __init__(self, **kws):
        self.namespaces = {}
        for name, uri in kws.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = f"{{uri}}"

    def __call__(self, path):
        return path.format_map(self.namespaces)


def main():
    """Main entry."""
    import os
    filename = os.path.join(os.path.dirname(__file__), "sample.xml")
    doc = parse(filename)
    ns = XMLNamespaces(html="http://www.w3.org/1999/xhtml")
    elem = doc.find(ns("content/{html}html"))
    print(elem)
    text = doc.findtext(ns("content/{html}head/{html}title"))
    print(text)


if __name__ == "__main__":
    main()

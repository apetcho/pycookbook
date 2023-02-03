#!/usr/bin/env python3
"""Example of reading an XML document, making changes, and writing it back out.
"""
from xml.etree.ElementTree import parse, Element


def main():
    """Main entry."""
    import os
    filename = os.path.join(os.path.dirname(__file__), "pred.xml")
    doc = parse(filename)
    root = doc.getroot()

    # -*- Remove a few elements -*-
    root.remove(root.find("sri"))
    root.remove(root.find("cr"))

    # -*- Insert a new element after <nm>...</nm>
    #nm_index = root.getchildren().index(root.find("nm"))
    nm = root.find("nm")
    elem = Element("spam")
    elem.text = "This is a test"
    if nm:
        #nm.insert(1, elem)
        nm.append(elem)
    
    #root.insert(nm_index+1, elem)

    # -*- Write back to a file
    newfname = os.path.join(os.path.dirname(__file__), "newpred.xml")
    doc.write(newfname, xml_declaration=True)


if __name__ == "__main__":
    main()

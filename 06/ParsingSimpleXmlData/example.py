#!/usr/bin/env python3
from urllib.request import urlopen
from xml.etree.ElementTree import parse


def main():
    """Main entry."""
    # -*- Download the RSS feed and parse it -*-
    resp = urlopen("http://planet.python.org/rss20.xml")
    doc = parse(resp)
    # -*- Extract and output tags of interest -*-
    for item in doc.iterfind("channel/item"):
        title = item.findtext("title")
        date = item.findtext("pubDate")
        link = item.findtext("link")
        print(f"{title}\n{date}\n{link}\n")


if __name__ == "__main__":
    main()

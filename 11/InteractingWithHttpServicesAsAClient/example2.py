#!/usr/bin/env python3
from urllib import request, parse
from pprint import pprint
import json


def main():
    """Main entry."""
    url = "http://httpbin.org/post"
    params = dict(name1="value1", name2="value2")
    query = parse.urlencode(params)
    fd = request.urlopen(url, query.encode("ascii"))
    response = fd.read()
    jsonresp = json.loads(response.decode("utf-8"))
    pprint(jsonresp)


if __name__ == "__main__":
    main()

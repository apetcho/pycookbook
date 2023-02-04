#!/usr/bin/env python3
from urllib import request, parse
from pprint import pprint
import json


def main():
    """Main entry."""
    url = "http://httpbin.org/get"
    params = {"name1": "value1", "name2": "value2"}
    querystr = parse.urlencode(params)
    urlfd = request.urlopen(f"{url}?{querystr}")
    response = urlfd.read()
    jsonresp = json.loads(response.decode("utf-8"))
    pprint(jsonresp)


if __name__ == "__main__":
    main()

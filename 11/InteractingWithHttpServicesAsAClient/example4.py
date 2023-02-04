#!/usr/bin/env python3
import requests


def main():
    """Main entry."""
    response = requests.head("http://www.python.org/index.html")
    status = response.status_code
    print(response.headers.keys())
    lastModified = response.headers["date"]
    #contentType = response.headers["Content-type"]
    contentLength = response.headers["content-Length"]
    for arg in (status, lastModified, contentLength):
        print(arg)


if __name__ == "__main__":
    main()

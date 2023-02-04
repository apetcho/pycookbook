#!/usr/bin/env python3
import requests
from pprint import pprint


def main():
    """Main entry."""
    url = "http://httpbin.org/post"
    params = dict(name1="value1", name2="value2")
    # -*- extra headers
    headers = {
        "User-agent": "none/ofyourbusiness",
        "Spam" : "Eggs",
    }
    response = requests.post(url, data=params, headers=headers)
    text = response.text
    # pprint(text)
    pprint(response.json)


if __name__ == "__main__":
    main()

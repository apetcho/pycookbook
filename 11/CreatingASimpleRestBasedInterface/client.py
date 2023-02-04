#!/usr/bin/env python3
from urllib.request import urlopen


def main():
    """Main entry."""
    fd = urlopen("http://localhost:8080/hello?name=Guido")
    print(fd.read().decode("utf-8"))
    fd = urlopen("http://localhost:8080/localtime")
    print(fd.read().decode("utf-8"))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- Example of *args and **kwargs functions -*-
import html


def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))


def make_element(name, value, **attrs):
    keyvals = [f" {key}={val}" for key, val in attrs.items()]
    attr_str = ''.join(keyvals)
    if attrs:
        element = "<{name}{attrs}>{value}</{name}>".format(
            name=name, attrs=attrs, value=html.escape(value)
        )
    else:
        element = "<{name}>{value}</{name}>".format(
            name=name, value=html.escape(value)
        )
    return element


def main():
    """Main entry."""
    print(avg(1, 2))
    print(avg(1, 2, 3, 4, 5))
    # -*- Example -*-
    # -*- Creates '<item size="large" quantity="6">Albatross</item>'
    print(make_element("item", "Albatross", size="large", quantity=6))
    print(make_element("p", "<spam>"))


if __name__ == "__main__":
    main()

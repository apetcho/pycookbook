#!/usr/bin/env python3
import weakref


class Spam:
    def __init__(self, name):
        self.name = name

_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        spam = Spam(name)
        _spam_cache[name] = spam
    else:
        spam = _spam_cache[name]
    return spam


def main():
    """Main entry."""
    a = get_spam("foo")
    b = get_spam("bar")
    print(f"a is b: {a is b}")
    c = get_spam("foo")
    print(f"a is c: {a is c}")


if __name__ == "__main__":
    main()

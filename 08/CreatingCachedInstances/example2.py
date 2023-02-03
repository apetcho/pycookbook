#!/usr/bin/env python3
import weakref


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            spam = Spam(name)
            self._cache[name] = spam
        else:
            spam = self._cache[name]
        return spam


class Spam:
    def __init__(self, name):
        self.name = name


Spam.manager = CachedSpamManager()


def get_spam(name):
    return Spam.manager.get_spam(name)


def main():
    """Main entry."""
    a = get_spam("foo")
    b = get_spam("bar")
    print(f"a is b: {a is b}")
    c = get_spam("foo")
    print(f"a is c: {a is c}")


if __name__ == "__main__":
    main()

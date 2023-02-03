#!/usr/bin/env python3
# Example of managed attributes via properties


class Person:
    def __init__(self, first_name:str):
        self.first_name = first_name

    @property
    def first_name(self):
        # -*- Getter function -*-
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value


def main():
    """Main entry."""
    guido = Person("Guido")
    print(guido)
    print(guido.first_name)
    guido.first_name = "Dave"
    print(guido.first_name)
    try:
        guido.first_name = 42
    except TypeError as err:
        print(err)


if __name__ == "__main__":
    main()

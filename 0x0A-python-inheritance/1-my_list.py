#!/usr/bin/python3
"""print_sorted module that inherits from ``list``."""


class MyList(list):
    """Child class that inherits from list parent class."""

    def print_sorted(self):
        print(sorted(self))

#!/usr/bin/python3
"""
This module, add_integer(a, b) adds 2 integers.
"""


def add_integer(a, b=98):
    """Returns the sum of 2 integers."""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

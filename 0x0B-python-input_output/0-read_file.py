#!/usr/bin/python3
"""read_file(filename="") module."""


def read_file(filename=""):
    """
    reads a text file (UTF8) & prints to stdout.

    Args:
        filename: the name of the text file.
    """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read())

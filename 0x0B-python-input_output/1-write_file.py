#!/usr/bin/python3
"""write_file(filename="", text="") module."""


def write_file(filename="", text=""):
    """
    writes str to text file & returns num of chars written.

    Args:
        filename: name of the text file.
        text: string to be written to text file.
    """
    with open(filename, 'w', encoding='utf-8') as a_file:
        return a_file.write(text)

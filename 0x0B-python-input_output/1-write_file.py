#!/usr/bin/python3
"""write_file(filename="", text="") module."""


def write_file(filename="", text=""):
    """
    writes str to text file & returns num of chars written.

    Args:
        filename: name of the text file.
        text: string to be written to text file.
    """
    with open(filename, mode='r+', encoding='utf-8') as a_file:
        a_file.write(text)
        count = 0
        for i in a_file:
            for j in i:
                count += 1
        return count

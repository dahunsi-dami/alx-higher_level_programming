#!/usr/bin/python3
"""append_write(filename="", text="") module."""


def append_write(filename="", text=""):
    """
    appends str to EOF & returns num of chars written.

    Args:
        filename: name of the text file.
        text: string to be appended to EOF.
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)

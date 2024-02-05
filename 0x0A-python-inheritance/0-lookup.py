#!/usr/bin/python3
"""Lookup module that give information on an object."""


def lookup(obj):
    """
    Returns available attributes and methods of an object.

    Args:
        obj: the parent class lookup inherits from.

    Returns:
        The available attributs and methods of an object.
    """
    return dir(obj)

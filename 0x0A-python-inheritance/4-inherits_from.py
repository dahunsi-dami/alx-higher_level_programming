#!/usr/bin/python3
"""inherits_from function."""


def inherits_from(obj, a_class):
    """
    returns True if obj is instance of a_class
    that inherits directly or indirectly from
    specified class.
    """

    if issubclass(obj.__class__, a_class) and (obj.__class__ != a_class):
        return True
    else:
        return False

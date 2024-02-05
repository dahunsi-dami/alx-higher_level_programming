#!/usr/bin/python3
"""is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """returns True if obj is instance of a_class
		or instance of instance of a_class."""

    if isinstance(obj, a_class):
        return True
    else:
        return False

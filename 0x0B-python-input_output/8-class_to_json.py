#!/usr/bin/python3
"""class_to_json(obj) module."""


def class_to_json(obj):

    """returns dict description w/ simple data structure
    (list, dict, str, int & boolean) for JSON serialization
    of an object."""

    return obj.__dict__

#!/usr/bin/python3
"""from_json_string(my_str) module."""

import json
"""import JSON module for encoding (serializing)
and decoding (deserializing)."""


def from_json_string(my_obj):
    """
    returns object (Python data structure) represented
    by JSON string.

    Args:
        my_str: JSON string to be decoded.
    """
    return json.loads(my_obj)

#!/usr/bin/python3
"""to_json_string(my_obj) module."""

import json
"""import JSON module for encoding (serializing)
and decoding (deserializing)."""


def to_json_string(my_obj):
    """
    returns JSON representation of an object (string).

    Args:
        my_obj: object to be represented in JSON.
    """
    return json.dumps(my_obj)

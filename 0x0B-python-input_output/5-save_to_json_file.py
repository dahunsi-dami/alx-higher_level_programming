#!/usr/bin/python3
"""save_to_json_file(my_obj, filename) module."""

import json
"""import JSON module for encoding (serializing)
and decoding (deserializing)."""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj: the Object to be written to a text file.
        filename: the text file Object should be written to.
    """
    json_object = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as a_file:
        a_file.write(json_object)

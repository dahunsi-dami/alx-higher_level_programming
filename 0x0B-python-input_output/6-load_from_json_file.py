#!/usr/bin/python3
"""load_from_json_file(filename) module."""

import json
"""import JSON module for encoding (serializing)
and decoding (deserializing)."""


def load_from_json_file(filename):
    """
    creates an Object from a JSON file.

    Args:
        filename: the JSON file Object should be created from.
    """
    with open(filename, "r", encoding="utf-8") as a_file:
        return json.load(a_file)

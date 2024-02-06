#!/usr/bin/python3
"""Empty class BaseGeometry."""


class BaseGeometry:
    """Raises exception message that
    area isn't implemented."""

    def area(self):
        raise Exception("area() is not implemented")

#!/usr/bin/python3
"""Empty class BaseGeometry."""


class BaseGeometry:
    """Raises exception message that
    area isn't implemented."""

    def area(self):
        """Raises exception that area isn't implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        self.name = name
        self.value = value

        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(self.name))

        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))

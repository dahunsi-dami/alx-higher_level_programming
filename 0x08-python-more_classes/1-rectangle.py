#!/usr/bin/python3
"""
Rectangle class definition.
"""


class Rectangle:
    """ Object representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialization of rectangle's attributes."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter alternative for private instance attribute width."""
        return self.__width

    @property
    def height(self):
        """getter alternative for private instance attribute height."""
        return self.__height

    @width.setter
    def width(self, value):
        """setter alternative for private instance attribute width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter alternative for private instance attribute height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

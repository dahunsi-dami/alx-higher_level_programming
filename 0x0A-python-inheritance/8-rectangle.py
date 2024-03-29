#!/usr/bin/python3
"""Rectangle class inheriting from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    "inherits from BaseGeometry."

    def __init__(self, width, height):
        """Instantiates private attributes width, height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

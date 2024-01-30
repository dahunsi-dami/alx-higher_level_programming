#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """ Object representation of a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of rectangle's attributes."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """calculates and returns area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates and returns perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns informal string representation of rectangle."""
        result = ""
        if self.__width != 0 and self.__height != 0:
            for y in range(self.__height):
                for x in range(self.__width):
                    result += str(self.print_symbol)
                result += "\n"
        return result

    def __repr__(self):
        """returns official string representation of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        klas = type(self).__name__
        return f"{klas}({self.__width}, {self.__height})"

    def __del__(self):
        """prints string when instance is deleted."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

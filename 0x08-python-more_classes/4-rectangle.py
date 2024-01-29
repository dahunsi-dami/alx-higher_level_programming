#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for y in range(self.__height):
            for x in range(self.__width):
                result += "#"
            result += "\n"
        return result

    def __repr__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        modl = type(self).__module__
        klas = type(self).__name__
        memad = hex(id(self))
        return f"{klas}({self.__width}, {self.__height})"

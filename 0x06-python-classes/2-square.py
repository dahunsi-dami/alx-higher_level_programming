#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""Square class definition."""


class Square:
    """A class defining a square shape.

    Attributes:
        __size (int): the size of one side of the square.

    """
    def __init__(self, size=0):
        """ The initialization of the square class.

        Args:
            size (int): the size of one side of the square.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

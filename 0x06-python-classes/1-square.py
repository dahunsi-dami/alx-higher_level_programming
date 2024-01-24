#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""Square class definition."""


class Square:
    """A class defining a square shape.

    Attributes:
        __size: the size of one side of the square.

    """
    def __init__(self, size):
        """ The initialization of the square class.

        Args:
            size: the size of one side of the square.

        """
        self.__size = size

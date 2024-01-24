#!/usr/bin/python3
# _*_ coding: utf-8 _*_
"""Square class definition."""


class Square:
    """A class defining a square shape.

    Attributes:
        size (int): the size of one side of the square.

    """
    def __init__(self, size=0):
        """The initialization of the square class.

        Args:
            size (int): the size of one side of the square.

        """
        self.size = size

    @property
    def size(self):
        """The getter method for private instance __size.

        Return:
            The size of the square object.

        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """The setter method for private instance __size.

        Args:
            size (int): the size of one side of the square.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance to get square area.

        Returns:
            The current square area.

        """
        return (self.__size) ** 2

    def my_print(self):
        """Public instance to print actual square.

        Returns:
            Nothing.

        """
        if (self.__size) == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format("#"), end="")
            print()

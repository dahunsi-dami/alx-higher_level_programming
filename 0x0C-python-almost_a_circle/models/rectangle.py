#!/usr/bin/python3
"""module defining child class Rectangle."""


from models.base import Base
"""imports Base from base.py in models folder."""


class Rectangle(Base):
    """nherits from base and defines a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates Rectangle's attributes."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

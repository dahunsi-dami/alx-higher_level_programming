#!/usr/bin/python3
"""module defining child class Rectangle."""


from models.base import Base
"""imports Base from base.py in models folder."""


class Rectangle(Base):
    """inherits from base and defines a rectangle."""

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area value of Rectangle instance."""
        return self.__height * self.__width

    def display(self):
        """prints in stdout rectangle instace with #."""
        if self.__y != 0:
            for i in range(self.__y):
                print()
        for line in range(self.__height):
            if self.__x != 0:
                for k in range(self.__x):
                    print(" ", end="")
                    if k == self.__x - 1:
                        for j in range(self.__width):
                            print("#", end="")
                        print()
            else:
                for row in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        """overrides __str__ method to return a string."""
        klas = type(self).__name__
        haid = self.id
        hx = self.__x
        hy = self.__y
        wit = self.__width
        hait = self.__height
        return f"[{klas}] ({haid}) {hx}/{hy} - {wit}/{hait}"

    def update(self, *args, **kwargs):
        """assigns an arg to each attribute,
        be it keyworded or non-keyworded."""
        arglist = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, arglist[i], arg)
        for k, v in kwargs.items():
            if k in arglist:
                setattr(self, k, v)

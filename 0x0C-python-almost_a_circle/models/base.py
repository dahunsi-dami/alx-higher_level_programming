#!/usr/bin/python3
"""module defining base class for other classes."""


class Base():
    """manages id attribute in child classes to avoid duplicates."""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiates public id attribute
            depending on id's value."""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

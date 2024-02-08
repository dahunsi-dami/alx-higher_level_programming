#!/usr/bin/python3
"""Class that defines a Student."""


class Student():
    """Definition of a student, as a class."""

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of Student class' attributes.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict representation of class object."""
        sd = {}
        if attrs is None:
            return self.__dict__
        else:
            if all(isinstance(elem, str) for elem in attrs):
                for i in attrs:
                    if i in self.__dict__:
                        sd.update({i: self.__dict__[i]})
                    else:
                        continue
                return sd

    def reload_from_json(self, json):
        """replaces all attributes of Student instance."""
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']

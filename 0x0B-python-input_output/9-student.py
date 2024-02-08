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

    def to_json(self):
        """retrieves dict representation of class object."""
        return self.__dict__

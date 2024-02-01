#!/usr/bin/python3
"""Class called LockedClass with no cls/other obj attribute"""


class LockedClass:
    """Class with only instance attribute first_name"""

    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = "first_name"

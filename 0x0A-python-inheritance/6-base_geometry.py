#!/usr/bin/python3
"""
This module contains a class BaseGeometry
with a public instance method.
"""


class BaseGeometry:
    """
    A class BaseGeometry with a public instance method.
    """

    def area(self):
        """
        A method that raises an Exception with
        the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

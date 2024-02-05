#!/usr/bin/python3
"""
This module contains a class BaseGeometry with public instance methods.
"""


class BaseGeometry:
    """
    A class BaseGeometry with public instance methods.
    """

    def area(self):
        """
        A method that raises an Exception with
        the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A method that validates value.

        Args:
            name: Always a string.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

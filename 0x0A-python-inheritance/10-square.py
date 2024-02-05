#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Constructor method.

        Args:
            size (int): The size of the Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

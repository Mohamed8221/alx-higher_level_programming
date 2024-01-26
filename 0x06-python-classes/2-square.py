#!/usr/bin/python3
""" Square module """


class Square:
    """This is a class Square that defines a square by size.
    """
    def __init__(self, size=0):
        """This is a method that initializes the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

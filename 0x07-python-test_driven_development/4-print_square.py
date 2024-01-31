#!/usr/bin/python3
""" 4-print_square Module """


def print_square(size):
    """
    Prints a square with the character #

    Parameters:
    size: the size length of the square

    Raises:
    TypeError: If size is not an integer or if size is a float and is less than 0
    ValueError: If size is less than 0
    """

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

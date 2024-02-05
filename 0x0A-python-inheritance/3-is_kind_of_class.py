#!/usr/bin/python3
"""
This module contains the function
is_kind_of_class that checks if an object is
an instance of, or if the object is an
instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of,
        or if the object is an instance of
        a class that inherited from,
        the specified class; otherwise False.
    """
    return isinstance(obj, a_class)

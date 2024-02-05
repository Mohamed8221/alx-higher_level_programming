#!/usr/bin/python3
"""
This module contains the function lookup that
returns the list of available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Function to return the list of available
    attributes and methods of an object.
    Args:
        obj: The object to inspect.

    Returns:
        A list of the attributes and methods of the object.
    """
    return dir(obj)

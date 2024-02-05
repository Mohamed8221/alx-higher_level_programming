#!/usr/bin/python3
"""
This module contains a function add_attribute
that adds a new attribute to an
object if it’s possible.
"""


def add_attribute(obj, name, value):
    """
    Function to add a new attribute to an object if it’s possible.

    Args:
        obj: The object to add the attribute to.
        name: The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can’t have new attribute.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

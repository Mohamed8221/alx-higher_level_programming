#!/usr/bin/python3
""" Module: 8-class_to_json """


def class_to_json(obj):
    """
    Function that returns the dictionary description.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary description of obj.
    """
    return obj.__dict__

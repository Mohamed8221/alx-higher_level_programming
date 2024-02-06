#!/usr/bin/python3
""" Module: 3-to_json_string """
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string).
    Args:
        my_str (str): The JSON string to convert to an object.
    Returns:
        str: The JSON string representation of my_obj.
    """
    return json.dumps(my_obj)

#!/usr/bin/python3
""" Module: 4-from_json_string """
import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    represented by a JSON string.
    Args:
        my_str (str): The JSON string to convert to an object.

    Returns:
        The object represented by my_str.
    """
    return json.loads(my_str)

#!/usr/bin/python3
""" Module: 6-load_from_json_file.py """
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        The object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

#!/usr/bin/python3
"""
Module: 0-read_file
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")

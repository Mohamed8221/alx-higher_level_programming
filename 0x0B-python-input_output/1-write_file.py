#!/usr/bin/python3
""" Module: 1-write_file """


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written.
    """

    with open(filename, 'w', encoding'utf-8') as f:
        return f.write(text)

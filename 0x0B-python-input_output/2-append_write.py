#!/usr/bin/python3
""" Module: 2-append_write """


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file
    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The text to append to the file. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

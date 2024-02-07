#!/usr/bin/python3
""" Module: 100-append_after """


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file,
    after each line containing a specific string.

    Args:
        filename (str): The name of the file. Defaults to "".
        search_string (str): The string to search for. Defaults to "".
        new_string (str): The new string to insert. Defaults to "".
    """
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

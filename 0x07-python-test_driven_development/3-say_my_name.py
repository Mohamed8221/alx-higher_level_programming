#!/usr/bin/python3
""" 3-say_my_name Module """


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"

    Parameters:
    first_name: a string
    last_name: a string

    Raises:
    TypeError: If first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

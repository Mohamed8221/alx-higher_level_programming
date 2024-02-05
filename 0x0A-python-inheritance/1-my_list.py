#!/usr/bin/python3
"""
This module contains the class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list.

    Methods:
        print_sorted: Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        A method that prints the list in ascending order.
        """
        print(sorted(self))

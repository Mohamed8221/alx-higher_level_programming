#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class MyInt that inherits from int
    and inverts the == and != operators.
    """

    def __eq__(self, other):
        """
        Inverted == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted != operator.
        """
        return super().__eq__(other)

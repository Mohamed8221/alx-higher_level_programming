#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Returns the addition of a and b

    Parameters:
    a: an integer or a float
    b: an integer or a float

    Returns:
    An integer: the addition of a and b

    Raises:
    TypeError: If a or b is not an integer or a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

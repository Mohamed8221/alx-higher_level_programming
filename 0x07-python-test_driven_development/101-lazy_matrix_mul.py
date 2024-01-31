#!/usr/bin/python3
""" 101-lazy_matrix_mul Module """


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module

    Parameters:
    m_a: a list of lists of integers or floats
    m_b: a list of lists of integers or floats

    Returns:
    A new matrix that is the result of the multiplication

    Raises:
    TypeError: If m_a or m_b is not a list, not a list of lists, contains non-integer/non-float values, or is not a rectangle (all rows are not of the same size)
    ValueError: If m_a or m_b is empty or if m_a and m_b can't be multiplied
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty" if m_a == [] or m_a == [[]] else "m_b can't be empty")

    # Check if all elements of m_a and m_b are integers or floats
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if all rows of m_a and m_b are of the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply m_a and m_b using NumPy
    return np.matmul(m_a, m_b)

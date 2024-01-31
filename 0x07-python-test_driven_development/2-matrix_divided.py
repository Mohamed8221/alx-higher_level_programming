#!/usr/bin/python3
""" 2-matrix_divided Module """


def matrix_divided(matrix, div):
    """
    Returns a new matrix that is the result of
    dividing all elements of the input matrix by div

    Parameters:
    matrix: a list of lists of integers or floats
    div: a number (integer or float)

    Returns:
    A new matrix

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats,
    if each row of the matrix does not have the same size, or if div
    is not a number
    ZeroDivisionError: If div is equal to 0
    """

    errMess = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(item, (int, float)) for row in matrix for item in row)):
        raise TypeError(errMess)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]

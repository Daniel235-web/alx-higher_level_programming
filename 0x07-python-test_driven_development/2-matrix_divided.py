#!/usr/bin/python3
"""This module contains a matrix division function"""

def matrix_divided(matrix, div):
    """This function divides all the elements of a matrix
    Params:
            matrix: a list of lists
            div: a divisor of type int/float
    Raises:
            TypeError: If the matrix contains non-numbers.
            TypeError: If the matrix contains rows of different sizes.
            TypeError: If div is not an int or float.
            ZeroDivisionError: If div is 0.
    Returns:
            new matrix with each elements being the result of the division of the old matrix and div
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    i =  0
    if matrix == None or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    while (i < len(matrix)):
        j = 0
        while (j < len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            j+= 1

        if i is not (len(matrix) - 1):
            if len(matrix[i]) is not len(matrix[i + 1]):
               raise TypeError("Each row of the matrix must have the same size")
        i+= 1

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]

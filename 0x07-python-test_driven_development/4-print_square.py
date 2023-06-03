#!/usr/bin/python3

"""This module contains a function that prints a square of a given size"""

def print_square(size):
    """This function prints a square of a given size
    args:
        size: size of square(integer)
    raise:
        ValueError: if size is less then 0
        TypeError: if size is not an integer
        TypeError: if size is a float and is less than 0
    return:
        void
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("\n".join(["#"*size for i in range(size)]))

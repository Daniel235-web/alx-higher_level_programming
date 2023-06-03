#!/usr/bin/python3

"""
    Module that contains a function that adds two integers


"""
def add_integer(a, b=98):
    """function that returns the addition of 2 integers 
	typecasts floats to ints
	raises error if a or b is not an integer"""
    errorMessage = ""
    if type(a) not in [int, float]:
        errorMessage = "a must be an integer"
    elif (type(a) == float):
            a = int(a)

    if type(b) not in [int, float] and (errorMessage == ""):
        errorMessage = "b must be an integer"
    elif (type(b) == float):
            b = int(b)

    if errorMessage == "":
        return (a + b)
    else:
        raise TypeError(errorMessage)


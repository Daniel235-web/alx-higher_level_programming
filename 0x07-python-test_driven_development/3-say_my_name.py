#!/user/bin/python3

"""This module contains a function that prints the first and last name of a user"""

def say_my_name(first_name, last_name=""):
    """This function prints the first and last name of a user
    Args:
        first_name: first name
        last_name: last name
    Raise:
        TypeError if first and/or last name is not a string
    Return:
        void
    """
    if type(first_name) != str :
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

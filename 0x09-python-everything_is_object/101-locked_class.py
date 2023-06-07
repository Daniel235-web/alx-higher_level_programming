#!/usr/bin/python3
"""This module defines a locked class."""


class LockedClass:
    """
    This class prevents a user from creating any attribute other than
    'first_name' for any instance of this class
    """

    __slots__ = ['first_name']

#!/usr/bin/python3
"""Function that returns list of available attributes and methods.
"""


def lookup(obj):
    """Method: list of attributes and methods of an object.

    Args:
    obj(object): instance

    Returns:
    List of available attributes and methods
    """
    return dir(obj)

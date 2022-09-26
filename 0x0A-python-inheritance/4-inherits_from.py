#!/usr/bin/python3
"""Function that retruns True or False.
"""


def inherits_from(obj, a_class):
    """Method: check instances of object.

    Args:
    obj: an object
    a_class: specified class

    Returns:
    True if obj is an instance of a_class, otherwise False
    """
    if type(obj) is a_class:
        return (False)
    return isinstance(obj, a_class)

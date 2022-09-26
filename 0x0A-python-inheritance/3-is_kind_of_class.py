#!/usr/bin/python3
"""Function that returns True or False.
"""


def is_kind_of_class(obj, a_class):
    """Method: check instances of object.

    Args:
    obj: an object
    a_class: specified class

    Return:
    True if obj is an instance of, or if obj is an instance of
    a class that inherited from, the specified class, otherwise False
    """
    return isinstance(obj, a_class)

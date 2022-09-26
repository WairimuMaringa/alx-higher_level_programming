#!/usr/bin/python3
"""Function that returns True or False.
"""


def is_same_class(obj, a_class):
    """Method: check instances of object.

    Args:
    obj(object): an object
    a_class(instance): specified class

    Return:
    True if obj is a_class, otherwise False
    """
    return type(obj) is a_class

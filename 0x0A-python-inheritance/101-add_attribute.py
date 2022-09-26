#!/usr/bin/python3
"""Function that adds new attribute to an object.
"""


def add_attribute(obj, att, value):
    """Method: add attribute to object if possible

    Args
    obj: object
    att: attribute
    value: attribute value
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
        return
    raise TypeError("can't add new attribute")

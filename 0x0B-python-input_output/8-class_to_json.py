#!/usr/bin/python3
"""Function that returns a dictionary description with simple data
structure (list, dictionary, string, integer and boolean."""


def class_to_json(obj):
    """Method: give dictionary rep for json serialization of obj

    Args:
    obj: object
    """
    dict_obj = dict()
    if hasattr(obj, '__dict__'):
        dict_obj = obj.__dict__.copy()
    return (dict_obj)

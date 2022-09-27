#!/usr/bin/python3
"""Function that returns the JSON representation of an
object(string)."""


import json


def to_json_string(my_obj):
    """Method: covert object to json string.

    Args:
    my_obj: object to convert
    """
    return (json.dumps(my_obj))

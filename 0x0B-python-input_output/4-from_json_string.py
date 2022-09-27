#!/usr/bin/python3
"""Function that returns an object(python data structure)
represented by a json string."""


import json


def from_json_string(my_str):
    """Method: convert object represented by json string

    Args:
    my_str: the json string
    """
    return (json.loads(my_str))

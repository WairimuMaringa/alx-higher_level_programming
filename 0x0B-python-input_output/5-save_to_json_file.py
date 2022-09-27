#!/usr/bin/python3
"""Function that writes an object to a text file using
JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    """Method: write object to text file

    Args:
    my_obj: object to be written
    filename: the file to write object to
    """
    with open(filename, mode="w", encoding="utf-8") as f_json:
        json.dump(my_obj, f_json)

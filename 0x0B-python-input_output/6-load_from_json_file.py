#!/usr/bin/python3
"""Function that creates an object from a json file.
"""


import json


def load_from_json_file(filename):
    """Method: create object from json file

    Args:
    filename: json file
    """
    with open(filename, mode="r", encoding="utf-8") as f_json:
        return (json.load(f_json))

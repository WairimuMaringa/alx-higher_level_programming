#!/usr/bin/python3
"""Class Base that manages id attributes of future classes.
"""
import json
import os.path
import csv


class Base:
    """Class Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

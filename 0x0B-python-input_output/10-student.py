#!/usr/bin/python3
"""Class student that defines a student.
"""


class Student:
    """class student: creates student instances"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if (type(attrs) is list and all(type(key) == str for key in attrs)):
            dict_obj = dict()
            for key in attrs:
                if hasattr(self, key):
                    dict_obj[key] = getattr(self, key)
            return (dict_obj)
        return (self.__dict__.copy())

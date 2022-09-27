#!/usr/bin/python3
"""Class Student that defines a student by firstname
lastname and age."""


class Student:
    """Class Student: defines a student
    """

    def __init__(self, first_name, last_name, age):
        """Method: create student

        Args:
        first_name: first name of student
        last_name: last name of student
        age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method: retrieve dictionary representation of student
        """
        return self.__dict__copy()

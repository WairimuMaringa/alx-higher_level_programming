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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        dict_base = []

        if list_objs is None or not list_objs:
            pass
        else:
            for instance in list_objs:
                dict_base.append(instance.to_dictionary())

        json_str = cls.to_json_string(dict_base)

        with open(filename, mode="w") as filejson:
            filejson.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            new_obj = cls(1)
        else:
            new_obj = cls(1, 1)
            new_obj.update(**dictionary)
            return (new_obj)

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename) is False:
            return (list())

        with open(filename, mode="r") as filejson:
            filecontent = filejson.read()

        list_dict = cls.from_json_string(filecontent)
        list_inst = list()

        for dic in list_dict:
            list_inst.append(cls.create(**dic))

        return (list_inst)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w") as filecsv:
            if list_objs is not None and list_objs:
                if cls.__name__ == "Rectangle":
                    labels = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    labels = ["id", "size", "x", "y"]
                writer = csv.DictWriter(filecsv, fieldname=labels)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        if os.path.isfile(filename) is False:
            return (list())

        with open(filename, mode="r") as filecsv:
            if cls.__name__ == "Rectangle":
                labels = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                labels = ["id", "size", "x", "y"]
            reader = csv.DictReader(filecsv, fieldnames=labels)

            list_dict = [dict([key, int(value)] for key, value in dic.items())
                         for dic in reader]
            list_inst = list()

            for dic in list_dict:
                list_inst.append(cls.create(**dic))

        return (list_inst)

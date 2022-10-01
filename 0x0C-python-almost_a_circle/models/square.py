#!/usr/bin/python3
"""Class square that is an inheritance of Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square: inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Method: create object square

        Args:
        size: size of square
        x: position x of square
        y: position y of square
        id: the id of square
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                self.id = (args[i] if i == 0 else self.id)
                self.size = (args[i] if i == 1 else self.size)
                self.x = (args[i] if i == 2 else self.x)
                self.y = (args[i] if i == 3 else self.y)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dict_squa = {"id": 0, "size": 0, "x": 0, "y": 0}
        for key in dict_squa.keys():
            dict_squa[key] = getattr(self, key)
        return (dict_squa)

    def __str__(self):
        str_squa = "({}) ".format(self.id)
        str_squa += "{}/{} - ".format(self.x, self.y)
        str_squa += "{}".format(self.size)
        return ("[Square] " + str_squa)

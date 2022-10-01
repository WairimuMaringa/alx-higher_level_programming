#!/usr/bin/python3
"""Class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle: inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: position x of the rectangle
            y: position y of the rectangle
            id: id of rectangle inherited from base
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        display_rect = ""
        display_rect += ("\n" * self.y)
        for i in range(self.height):
            display_rect += (" " * self.x)
            display_rect += ("#" * self.width)
            display_rect += ("\n")
        print(display_rect, end="")

    def __str__(self):
        str_rect = "({}) ".format(self.id)
        str_rect += "{}/{} - ".format(self.x, self.y)
        str_rect += "{}/{}".format(self.width, self.height)
        return ("[Rectangle] " + str_rect)

    def update(self, *args, **kwargs):
        if args is not None and len(args) > 0:
            for i in range(len(args)):
                self.id = (args[i] if i == 0 else self.id)
                self.width = (args[i] if i == 1 else self.width)
                self.height = (args[i] if i == 2 else self.height)
                self.x = (args[i] if i == 3 else self.x)
                self.y = (args[i] if i == 4 else self.y)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        dict_rect = {"id": 0, "width": 0, "height": 0, "x": 0, "y": 0}
        for key in dict_rect.keys():
            dict_rect[key] = getattr(self, key)
        return (dict_rect)

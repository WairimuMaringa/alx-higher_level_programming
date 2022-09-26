#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle: inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """Method: construct rectangle.

        Args:
        width(int): width of rectangle
        height(int): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method: area of rectangle

        Returns:
        the area of rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Method: returns a printable string

        Returns:
        the string format of the rectangle
        """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

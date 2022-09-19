#!/usr/bin/python3
"""Defines an object rectangle.
"""


class Rectangle:
    """Class Rectangle empty.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Method: initialize.

        Args:
        width(int): width of rectangle
        height(int): height of rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        drawn = ""
        if self.height != 0 and self.width != 0:
            for i in range(self.height):
                drawn += (str(self.print_symbol) * self.width) + "\n"
        return (drawn[:-1])

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

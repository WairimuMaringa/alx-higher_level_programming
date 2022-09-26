#!/usr/bin/python3
"""Class Square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square: inherits from Rectangle
    """

    def __init__(self, size):
        """Method: construct rectangle

        Args:
        size(int): size of rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method: returns a string with the area
        """
        return super().area()

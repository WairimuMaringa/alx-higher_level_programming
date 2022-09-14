#!/usr/bin/python3
"""Class Square that defines a square by size.
"""


class Square:
    """Class Square
    """
    def __init__(self, size=0):
        """Method: initialization.

        Args:
        size(int): size of the square
        self(class): the class
        """
        self.size = size

    def area(self):
        """Method: return the square area.

        Args:
        self(class): the class
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Method: return size value.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method: set size value of the square object.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

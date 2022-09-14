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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


def area(self):
    """Method that returns the square area.

    Args:
    self(class): the class
    """
    return (self.__size ** 2)

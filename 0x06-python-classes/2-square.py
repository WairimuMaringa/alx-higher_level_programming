#!/usr/bin/python3
"""Class Square that defines a square by size.
"""


class Square:
    """Class Square
    """
    def __init(self, size=0):
        """Initialize method

        Args:
        size(int): size of the square
        self(class): the class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

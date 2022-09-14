#!/usr/bin/python3
"""Class Square that defines a square by size.
"""


class Square:
    """Class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Method: initialization.

        Args:
        size(int): size of the square
        self(class): the class
        """
        self.size = size
        self.position = position

    def area(self):
        """Method: return the square area.

        Args:
        self(class): the class
        """
        return (self.__size ** 2)

    def my_print(self):
        """Method: print in stdout the square with the character #.

        Args:
        self(class): the class
        """
        if self.__size:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()

    @property
    def size(self):
        """Method: returns the size value.
        """
        return (self.__size)

    @property
    def position(self):
        """Method: returns the position value.
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """Method: set size value of the square object.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Method: set position value of square object.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

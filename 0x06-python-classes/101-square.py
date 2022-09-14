#!/usr/bin/python3
"""Class Square that defines a square.
"""


class Square:
    """Class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()

    def __str__(self):
        rtrn = ""
        if self.__size:
            for i in range(self.position[1]):
                rtrn += "\n"
            for j in range(self.size):
                rtrn += " " * self.position[0]
                rtrn += "#" * self.size
                if j != (self.size - 1):
                    rtrn += "\n"
        return (rtrn)

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

#!/usr/bin/python3
"""Class MyList that inherits from list.
"""


class MyList(list):
    """Class: Inherit from list

    Args:
    list(list): the list
    """

    def print_sorted(self):
        """Method: Prints the list in a sorted way(ascending sort).
        """
        list_sorted = self.copy()
        list_sorted.sort()
        print(list_sorted)

#!/usr/bin/python3
"""Class MyList that inherits from list.
"""


class MyList(list):
    """Method: Inherit from list.

    Args:
    list(list): the list
    """

    def print_sorted(self):
        """Prints the list in a sorted (ascending) manner.
        """
        print(sorted(self))

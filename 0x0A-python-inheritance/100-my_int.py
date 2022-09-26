#!/usr/bin/python3
"""Class MyInt htat inherits from int.
"""


class MyInt(int):
    """Class MyInt: inherit from int
    """

    def __eq__(self, other):
        """Method: invert == for !=
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Method: invert != for ==
        """
        return int.__eq__(self, other)

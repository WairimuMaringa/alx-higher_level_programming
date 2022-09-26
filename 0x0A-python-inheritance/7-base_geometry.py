#!/usr/bin/python3
"""An empty class BaseGeometry.
"""


class BaseGeometry:
    """Class: BaseGeometry
    """

    def area(self):
        """Method: define area of shape.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method: validate value.

        Args:
        name(str): string value
        value(int) integer value
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

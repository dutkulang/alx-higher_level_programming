#!/usr/bin/python3

"""
Adding a and b
a and b must be neither int or float
the result is typecasted to float
"""


def add_integer(a, b=98):

    """Return sum of a and b
    Floats must be typecasted to integers
    Raises: TypeError: If a or b is not an integer or float"""

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    elif (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

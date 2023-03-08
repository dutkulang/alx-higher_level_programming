#!/usr/bin/python3

"""
say_my_name prints out the first and last name passed to it.

"""


def say_my_name(first_name, last_name=""):

    """
    Return the first and last name
    Raises TypeError if first name or last name are not strings.
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")

    elif (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

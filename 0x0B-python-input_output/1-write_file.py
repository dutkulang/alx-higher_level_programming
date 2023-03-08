#!/usr/bin/python3

"""Defining a program to write to a file"""


def write_file(filename="", text=""):
    """ writing text to a file"""
    with open(filename, "w") as file:
        return file.write(text)

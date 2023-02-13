#!/usr/bin/python3
""" Defines a text reading function"""


def read_file(filename=""):
    """reads the content of a files and prints it on to the screen"""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

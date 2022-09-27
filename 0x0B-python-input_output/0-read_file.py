#!/usr/bin/python3
"""Function that reads a text file UTF8 and prints to stdout.
"""


def read_file(filename=""):
    """Method: read from UTF8 and print to stdout

    Args:
    filename: the filename
    """
    with open(filename, mode="r", encoding="utf-8") as f_txt:
        print(f_txt.read(), end='')

#!/usr/bin/python3
"""Function that appends a string at the end of a textfile and
returns number of characters added."""


def append_write(filename="", text=""):
    """Method: append a string at the end of UTF8

    Args:
    filename: the filename
    text: string to be written
    """
    with open(filename, mode="a", encoding="utf-8") as f_append:
        return (f_append.write(text))

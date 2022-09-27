#!/usr/bin/python3
"""Function that writes a string to a text file and returns
the number of characters given."""


def write_file(filename="", text=""):
    """Method: write a string to UTF8 textfile

    Args:
    filename: file name
    text: string to be written to file
    """
    with open(filename, mode="w", encoding="utf-8") as f_new:
        return (f_new.write(text))

#!/usr/bin/python3
"""Function tht inserts line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Method: inserts line of text to a file

    Args:
    filename: name of the file
    search_string: string to search in the file
    new_string: string to be added
    """
    new_content = ""
    with open(filename, mode="r") as old_file:
        for line in old_file:
            new_content += line
            if search_string in line:
                new_content += new_string

    with open(filename, mode="w") as new_file:
        new_file.write(new_content)

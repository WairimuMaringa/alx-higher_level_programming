#!/usr/bin/python3
""" Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    half = int(length / 2)

    if half + 1 >= length and half - 1 < 0:
        return list_of_integers[half]
    elif half - 1 < 0:
        if list_of_integers[half] > list_of_integers[half + 1]:
            return list_of_integers[half]
        else:
            return list_of_integers[half + 1]
    elif half + 1 >= length:
        if list_of_integers[half] > list_of_integers[half - 1]:
            return list_of_integers[half]
        else:
            return list_of_integers[half - 1]

    if (
            list_of_integers[half - 1] < list_of_integers[half] and
            list_of_integrs[half] > list_of_integers[half + 1]
    ):
        return list_of_integers[half]

    if list_of_integers[half + 1] > list_of_integers[half - 1]:
        return find_peak(list_of_integers[half:])

    return find_peak(list_of_integers[:half])

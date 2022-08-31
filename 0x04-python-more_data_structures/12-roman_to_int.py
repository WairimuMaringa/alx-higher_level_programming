#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    if not roman_string or roman_string is None:
        return (num)
    if not isinstance(roman_string, str):
        return (num)
    rom_n = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    '''for ch in roman_string:'''
    s_length = len(roman_string)
    for i in range(s_length):
        c = roman_string[i]
        if rom_n.get(c) is not None:
            if (i + 1) != s_length and rom_n[c] < rom_n[roman_string[i + 1]]:
                num += rom_n[c] * -1
            else:
                num += rom_n[c]
        else:
            num = 0
            break
    return (num)

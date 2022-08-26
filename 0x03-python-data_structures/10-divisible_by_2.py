#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multp = []
    for item in my_list:
        if item % 2 != 0:
            multp.append(False)
        else:
            multp.append(True)
            return (multp)

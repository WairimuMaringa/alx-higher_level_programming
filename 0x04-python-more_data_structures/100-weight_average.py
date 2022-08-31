#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or my_list is None:
        return (0)
    num1 = 0
    num2 = 0
    for tupl in my_list:
        num1 += tupl[0] * tupl[1]
        num2 += tupl[1]
    return (num1 / num2)

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult_2 = a_dictionary.copy()
    for key in mult_2:
        mult_2[key] = mult_2[key] * 2
    return mult_2

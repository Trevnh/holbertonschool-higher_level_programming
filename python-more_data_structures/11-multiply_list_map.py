#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = list(my_list)
    for item in range(0, len(new_list)):
        new_list[item] *= number
    return new_list

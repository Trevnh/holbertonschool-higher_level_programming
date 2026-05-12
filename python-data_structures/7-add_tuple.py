#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        temp_tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        temp_tuple_a = (tuple_a[0], 0)
    else:
        temp_tuple_a = (tuple_a[0], tuple_a[1])
    if len(tuple_b) == 0:
        temp_tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        temp_tuple_b = (tuple_b[0], 0)
    else:
        temp_tuple_b = (tuple_b[0], tuple_b[1])
    a = temp_tuple_a[0] + temp_tuple_b[0]
    b = temp_tuple_a[1] + temp_tuple_b[1]
    tuple_c = (a, b)
    return tuple_c

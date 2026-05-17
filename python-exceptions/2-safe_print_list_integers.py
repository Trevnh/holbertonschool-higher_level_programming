#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    skip = 0
    while length < x:
        try:
            print("{:d}".format(my_list[length]), end="")
            length += 1
        except (ValueError, TypeError):
            length += 1
            skip += 1
            pass
    print()
    return (length - skip)

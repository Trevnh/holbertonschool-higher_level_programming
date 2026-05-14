#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = []
    common = []
    for item1 in set_1:
        for item2 in set_2:
            if item1 == item2:
                common.append(item1)
    for item1 in set_1:
        for item2 in common:
            if item1 != item2:
                od_set.append(item1)
    for item1 in set_2:
        for item2 in common:
            if item1 != item2:
                od_set.append(item1)
    return od_set

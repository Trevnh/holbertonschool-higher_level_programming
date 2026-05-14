#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = 0
    for key in a_dictionary:
        if a_dictionary[key] > best:
            best = a_dictionary[key]
            best_scorer = key
    return best_scorer

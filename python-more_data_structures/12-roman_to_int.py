#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_val = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    if not roman_string or not isinstance(roman_string, str):
        return result
    for i in range(0, len(roman_string)):
        if (i == len(roman_string) - 1 or
            roman_val[roman_string[i]] >= roman_val[roman_string[i+1]]):
            result += roman_val[roman_string[i]]
        else:
            result -= roman_val[roman_string[i]]
    return result

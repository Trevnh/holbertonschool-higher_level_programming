#!/usr/bin/python3
"""Module for script that adds all arguments
to a Python list and saves to a file"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

try:
    file_list = load_from_json_file(filename)
except FileNotFoundError:
    file_list = []

file_list.extend(sys.argv[1:])

save_to_json_file(file_list, filename)

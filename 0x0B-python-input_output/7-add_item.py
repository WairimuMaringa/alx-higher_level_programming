#!/usr/bin/python3
"""Add arguments to a python file and save them to
a file."""


import sys
import os


save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
my_list = []

if os.path.isfile(filename):
    my_list = load_file(filename)

for item in sys.argv[1:]:
    my_list.append(item)

save_file(my_list, filename)

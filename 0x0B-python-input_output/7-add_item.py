#!/usr/bin/python3
""" Module: 7-add_item """
import sys
import os

sFile = __import__("5-save_to_json_file").save_to_json_file
lFile = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
if path.exists(filename):
    my_list = lFile(filename)
else:
    my_list = []
my_list.extend(sys.argv[1:])
sFile(my_list, filename)


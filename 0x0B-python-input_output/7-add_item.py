#!/usr/bin/python3
""" Module: 7-add_item """
import sys
from os import path
import importlib

sFile_module = importlib.import_module('5-save_to_json_file')
lFile_module = importlib.import_module('6-load_from_json_file')

filename = "add_item.json"
if path.exists(filename):
    my_list = lFile_module.load_from_json_file(filename)
else:
    my_list = []
my_list.extend(sys.argv[1:])
sFile_module.save_to_json_file(my_list, filename)

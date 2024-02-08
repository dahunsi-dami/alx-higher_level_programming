#!/usr/bin/python3
"""adds all arguments of Python list to JSON file."""

import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    filename = "add_item.json"
    plist = []
    arg_lent = len(sys.argv)
    i = 1

    try:
        plist = load_from_json_file(filename)
    except IOError:
        pass

    while i < arg_lent:
        plist.append(sys.argv[i])
        i += 1

    save_to_json_file(plist, filename)

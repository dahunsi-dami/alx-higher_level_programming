#!/usr/bin/python3
def element_at(my_list, idx):
    llen = len(my_list)
    if idx < 0 or idx >= llen:
        return "None"
    else:
        return my_list.pop(idx)

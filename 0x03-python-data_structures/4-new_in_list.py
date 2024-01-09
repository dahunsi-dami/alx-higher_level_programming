#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    llen = len(my_list)
    if idx < 0 or idx >= llen:
        return my_list
    cop = my_list.copy()
    cop.pop(idx)
    cop.insert(idx, element)
    return cop

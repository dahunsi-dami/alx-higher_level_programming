#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    llen = len(my_list)
    if idx < 0 or idx >= llen:
        return my_list
    else:
        my_list.pop(idx)
        my_list.insert(idx, element)
        cop = my_list.copy()
        return cop

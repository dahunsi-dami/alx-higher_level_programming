#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is not None:
        llen = len(my_list)
        if idx < 0 or idx >= llen:
            return my_list
        del my_list[idx]
        return my_list

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    llen = len(my_list)
    nlist = my_list.copy()
    i = 0
    while i < llen:
        if nlist[i] == 2:
            nlist[i] = 89
        i += 1
    return nlist

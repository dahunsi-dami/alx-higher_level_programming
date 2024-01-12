#!/usr/bin/python3
def search_replace(my_list, search, replace):
    llen = len(my_list)
    nlist = my_list.copy()
    i = 0
    while i < llen:
        if nlist[i] == search:
            nlist[i] = replace
        i += 1
    return nlist

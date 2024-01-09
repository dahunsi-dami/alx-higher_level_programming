#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        nl = []
        llen = len(my_list)
        i = 0
        while i < llen:
            if my_list[i] % 2 == 0:
                nl.append(True)
            else:
                nl.append(False)
            i += 1
        return nl

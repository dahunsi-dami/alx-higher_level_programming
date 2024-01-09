#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    nl = my_list.copy()
    print(nl)
    llen = len(nl)
    i = 0
    while i < llen:
        if i == 7:
            if nl[i] < nl[i - 1]:
                temp = nl[i]
                nl[i] = nl[i - 1]
                nl[i - 1] = temp
        else:
            j = nl[i]
            max = nl[i + 1]
            if j > max:
                temp = nl[i]
                nl[i] = max
                nl[i + 1] = temp
        i = i + 1
    hi = nl[-1]
    return hi

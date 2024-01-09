#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    llen = len(my_list)
    i = 0
    while i < llen:
        if i == 7:
            if my_list[i] < my_list[i - 1]:
                temp = my_list[i]
                my_list[i] = my_list[i - 1]
                my_list[i - 1] = temp
        else:
            j = my_list[i]
            max = my_list[i + 1]
            if j > max:
                temp = my_list[i]
                my_list[i] = max
                my_list[i + 1] = temp
        i = i + 1
    hi = my_list[-1]
    return hi

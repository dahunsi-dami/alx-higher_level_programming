#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_s = set(my_list)
    for i in my_s:
        sum += i
    print(my_list)
    print(my_s)
    return sum

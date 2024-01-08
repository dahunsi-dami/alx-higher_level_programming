#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    cop = my_list.copy()
    cop.reverse()
    for i in cop:
        print("{:d}".format(i))

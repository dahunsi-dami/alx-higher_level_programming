#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    llen = len(my_list) - 1
    while (llen >= 0):
        print("{:d}".format(my_list[llen]))
        llen = llen - 1

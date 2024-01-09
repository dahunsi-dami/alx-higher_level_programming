#!/usr/bin/python3
def no_c(my_string):
    my_string = my_string.translate({99: 0})
    my_string = my_string.translate({67: 0})
    return my_string

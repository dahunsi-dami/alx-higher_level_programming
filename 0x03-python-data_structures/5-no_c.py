#!/usr/bin/python3
def no_c(my_string):
    result = my_string.translate({99: 0})
    sresult = result.translate({67: 0})
    return sresult

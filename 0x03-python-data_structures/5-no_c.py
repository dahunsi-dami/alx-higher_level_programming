#!/usr/bin/python3
def no_c(my_string):
    nstring = my_string.translate({ord("c"): None})
    nstring = nstring.translate({ord("C"): None})
    return nstring

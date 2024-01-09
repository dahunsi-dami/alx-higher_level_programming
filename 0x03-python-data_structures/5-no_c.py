#!/usr/bin/python3
def no_c(my_string):
    nstring = my_string.translate({99: None})
    nstring = nstring.translate({67: None})
    return nstring

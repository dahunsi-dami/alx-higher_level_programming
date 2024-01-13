#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndict = a_dictionary.copy()
    for k, v in ndict.items():
        ndict[k] = v * 2
    return ndict

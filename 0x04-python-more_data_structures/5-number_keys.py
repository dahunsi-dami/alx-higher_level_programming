#!/usr/bin/python3
def number_keys(a_dictionary):
    nkeys = 0
    for k, v in a_dictionary.items():
        nkeys += 1
    return nkeys

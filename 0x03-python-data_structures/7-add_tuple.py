#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = len(tuple_a)
    lb = len(tuple_b)
    if la == 0:
        tuple_a = tuple_a + (0, 0, )
    if la == 1:
        tuple_a = tuple_a + (0, )
    if lb == 0:
        tuple_b = tuple_b + (0, 0, )
    if lb == 1:
        tuple_b = tuple_b + (0, )
    nt = ()
    for i in range(0, 2):
        z = tuple_a[i] + tuple_b[i]
        nt = nt + (z, )
    return nt

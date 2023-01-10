#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        a = tuple_a[0]
        b = 0
    else:
        a, b = tuple_a
    if len(tuple_b) < 2:
        c = tuple_b[0]
        d = 0
    else:
        c, d = tuple_b
    return (a + c, b + d)

#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    dup = my_list[:]

    if 0 <= idx < len(my_list):
        dup[idx] = element
        return dup
    return my_list

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    ls = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            ls.append(True)
        else:
            ls.append(False)
    return ls

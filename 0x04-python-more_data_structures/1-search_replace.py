#!/usr/bin/python3

def search_replace(my_list, search, replace):
    arrL = len(my_list)
    new_list = my_list.copy()

    i = 0
    while i < arrL:
        if new_list[i] == search:
            new_list[i] = replace
        i += 1
    return new_list

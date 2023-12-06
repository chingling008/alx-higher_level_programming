#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set()
    result = 0

    for i in range(len(my_list)):
        if all(my_list[i] != my_list[j] for j in range(i)):
            result += my_list[i]
            unique_numbers.add(my_list[i])

    return result

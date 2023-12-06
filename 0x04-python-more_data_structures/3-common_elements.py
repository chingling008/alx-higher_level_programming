#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_set = set()

    iterator_1 = iter(set_1)
    while True:
        try:
            element = next(iterator_1)
            if element in set_2:
                common_set.add(element)
        except StopIteration:
            break

    return common_set

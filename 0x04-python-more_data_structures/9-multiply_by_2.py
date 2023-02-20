#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = []
    b = dict()
    count = 0
    for value in a_dictionary.values():
        a.append(value * 2)
    for key in a_dictionary.keys():
        b[key] = a[count]
        count += 1
    return b
    
#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    a = []
    if len(my_list) == 0:
        return my_list
    for i in my_list:
        a.append(i)

    if idx >= len(a):
        return a
    elif idx < 0:
        return a
    else:
        a[idx] = element
        return a

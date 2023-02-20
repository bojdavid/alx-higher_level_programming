#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    a = []
    for i in my_list:
        a.append(i)

    if idx >= len(a):
        return a
    elif idx < 0:
        return a
    else:
        a[idx] = element
        return a

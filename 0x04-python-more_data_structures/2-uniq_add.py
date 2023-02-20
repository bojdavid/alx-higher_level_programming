#!/usr/usr/python3
def uniq_add(my_list=[]):
    a = []
    sum = 0
    for i in my_list:
        if i in a:
            continue
        else:
            a.append(i)
    for i in a:
        sum = sum + i
    return sum
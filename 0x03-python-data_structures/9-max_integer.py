#!/usr/bin/python3
def max_integer(my_list=[]):
    if bool(my_list) is False:
        return None
    max1 = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max1:
            max1 = my_list[i]
    return max1

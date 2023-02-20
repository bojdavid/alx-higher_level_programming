#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    union = set()
    for i in set_1:
        union.add(i)
    for i in set_2:
        union.add(i)
    return union
   
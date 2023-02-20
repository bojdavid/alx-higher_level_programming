#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = set()
    b = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                a.add(i)
    for i in set_1:
        if i not in a:
            b.add(i)
    for i in set_2:
        if i not in a:
            b.add(i)
    return b

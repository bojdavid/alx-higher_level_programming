#!/usr/bin/python3

def remove_char_at(str, n):
    count = 0
    a = []
    for i in str:
        if count == n:
            count += 1
            continue
        else:
            a.append(i)
            count += 1
    return ''.join(a)

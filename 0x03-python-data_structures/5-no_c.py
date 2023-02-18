#!/usr/bin/python3

def no_c(my_string):
    a = []
    for i in my_string:
        a.append(i)
    
    for j in a:
        if j == 'c' or j == 'C':
            a.remove(j)
    return ''.join(a)
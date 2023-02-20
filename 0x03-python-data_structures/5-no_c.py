#!/usr/bin/python3

def no_c(my_string):
    a = []
    for i in my_string:
        a.append(i)
    
    for j in a:
        if j == 'c':
            a.remove('c')
        elif j == 'C':
            a.remove('C')

    return ''.join(a)

a = "HellcCcccooccoscccss"
print(no_c(a))
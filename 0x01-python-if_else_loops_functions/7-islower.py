#!/usr/bin/python3

def islower(c):
    for i in range (97,123):
        if c != chr(i):
            a = False
        else:
            a = True
            break
    return a

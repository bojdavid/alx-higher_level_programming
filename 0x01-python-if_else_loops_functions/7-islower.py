#!/usr/bin/python3

def islower(c):
    for i in range (97,123):
        if c != chr(i):
            for j in range(65, 91):
                if c == chr(j):
                    a = False
                    break
        else:
            a = True
    return a

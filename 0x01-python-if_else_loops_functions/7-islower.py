#!/usr/bin/python3

def islower(c):
    if type(c) == str:
        for i in range (97,123):
            if c != chr(i):
                        a = False
            else:
                a = True
                break
        return a
    else:
        raise Error("value is not a string")

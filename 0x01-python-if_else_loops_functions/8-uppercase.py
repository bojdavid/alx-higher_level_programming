#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if ord(i) in range(97, 122):
            up = ord(i) - 32
            print('{}'.format(chr(up)), end='')
        else:
            print('{}'.format(i), end='')

#!/usr/bin/python3

def uppercase(str):
    for i in str:
        up = i
        if ord(i) in range(97, 123):
            up = chr(ord(i) - 32)
        print('{}'.format(up), end='')
    print('')

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        a = []
        for i in range(0, x):
            a.append(my_list[i])
            count += 1
        for i in a:
            print("{:d}".format(i), end='')
        print("")
        return count
    except IndexError as e:
        count = 0
        for i in my_list:
            print("{:d}".format(i), end='')
            count += 1
        print("")
        return count

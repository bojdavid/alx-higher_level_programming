#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(0, x):
            if type(my_list[i]) == int:
                print('{:d}'.format(my_list[i]), end='')
                count += 1
            else:
                continue
        print("")
        return count
    except Exception as e:
        print(e)

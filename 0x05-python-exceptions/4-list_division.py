#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except Exception as e:
            print(e)
            div = 0
        finally:
            a.append(div)
    return a

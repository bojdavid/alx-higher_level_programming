#!/usr/bin/python3
def weight_average(my_list=[]):
    if bool(my_list) is False:
        return None
    else:
        sum = 0
        no = 0
        for i in my_list:
            mul = i[0] * i[1]
            sum = sum + mul
            no = no + i[1]
        return (sum / no)

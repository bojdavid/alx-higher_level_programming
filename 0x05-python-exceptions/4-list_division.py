#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    a = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except ArithmeticError as e:
            print('division by 0')
            div = 0
        except TypeError as e:
            print('wrong type')
            div = 0
        except IndexError as e:
            print('out of range')
            div = 0
        finally:
            a.append(div)
    return a

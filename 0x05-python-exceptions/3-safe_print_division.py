#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except ArithmeticError as e:
        print(e)
    finally:
        print('Inside result: {}'.format(c))
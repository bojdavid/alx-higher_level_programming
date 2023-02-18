#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    
    for i in matrix:
        count = 0
        for j in i:
            if count < len(i):
                print('{:d}'.format(j), end=' ')
            if count == len(i):
                print('{:d}'.format(j), end='')
            count += 1
        print('')

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
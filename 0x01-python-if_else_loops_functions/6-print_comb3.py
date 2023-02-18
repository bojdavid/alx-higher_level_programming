#!/usr/bin/python3
count = 0
for i in range(0, 10):
    for j in range(0, 10):
        if i >= j:
            continue
        else:
            if count > 0:
                print(',', end=' ')
            print("{}{}".format(i, j), end='')
        count += 1
print('')

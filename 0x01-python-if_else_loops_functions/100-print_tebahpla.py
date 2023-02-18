#!/usr/bin/python3

count = 1
for i in reversed(range(97, 123)):
    if (count % 2) == 0:
        a = chr(i - 32)
    else:
        a = chr(i)
    print('{}'.format(a), end='')
    count += 1
	

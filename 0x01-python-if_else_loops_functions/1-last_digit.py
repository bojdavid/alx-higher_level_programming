#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    sign = -1
else:
    sign = 1
num = number * sign
a = str(num)
for i in a:
    last_digit = int(i) * sign

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

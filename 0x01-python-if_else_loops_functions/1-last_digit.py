#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = number * -1
    n = n % 10
    n = n * -1
else:
    n = number % 10
print("Last digit of {}".format(number), end=' ')
if n > 5:
    print("is {} and is greater than 5".format(n))
elif n == 0:
    print("is {} and is 0".format(n))
elif n < 6 and n != 0:
    print("is {} and is less than 6 and not 0".format(n))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_last = number % 10
if number_last > 5:
    print('Last digit of ' + str(number) + ' is ' + str(number_last) + ' and is greater than 5')
elif number_last == 0:
    print('Last digit of ' + str(number) + ' is ' + str(number_last) + ' and is 0')
elif number_last < 6 and number_last != 0:
    print('Last digit of ' + str(number) + ' is ' + str(number_last) + ' and is less than 6 and not 0')

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Digit = number % -10
else:
    Digit = number % 10
if Digit > 5:
    print(f"Last digit of {number} is {Digit} and is greater than 5")
elif Digit == 0:
    print(f"Last digit of {number} is {Digit} and is 0")
elif Digit < 6:
    print(f"Last digit of {number} is {Digit} and is less than 6 and not 0")

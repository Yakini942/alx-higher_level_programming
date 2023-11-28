#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Do not modify the code above this line
# Complete the code below to print whether the number is positive, negative,

print(number)

if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")


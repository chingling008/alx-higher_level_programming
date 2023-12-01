#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnumber = str(number)
lastDigit = strnumber[len(strnumber)-1]
intLast = int(lastDigit)
if intLast == 0:
    print("Last digit of " + strnumber + " is " + 
            lastDigit + " and is 0")
elif number < 1:
    print("Last digit of " + strnumber + " is -" + lastDigit + " and is less than 6 and not 0")
elif intLast > 5:
    print("Last digit of " + strnumber + " is " + lastDigit + " and is greater than 5")
elif intLast < 6:
    print("Last digit of " + strnumber + " is " + lastDigit + " and is less than 6 and not 0")

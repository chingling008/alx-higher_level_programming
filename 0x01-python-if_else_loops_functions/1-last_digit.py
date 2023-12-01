#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnumber = str(number)
lastDigit = strnumber[len(strnumber)-1]
intLast = int(lastDigit)
if intLast == 0:
    print("Last Digit of " + strnumber + " is " + lastDigit + " is 0")
elif number < 1:
    print("Last Digit of " + strnumber + " is -" + lastDigit + " is less than 6 and not 0")
elif intLast > 5:
    print("Last Digit of " + strnumber + " is " + lastDigit + " is greater than 5")
elif intLast < 6:
    print("Last Digit of " + strnumber + " is " + lastDigit + " is less than 6 and not 0")

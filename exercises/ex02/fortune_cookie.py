"""Fortune_Cookies."""

__author__ = "730390549"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")

a: int = randint(0, 5)

if a == 0:
    print("Fortune is coming your way")
else:
    if a == 1:
        print("Someone is speaking well of you")
    else:
        if a == 2:
            print("You are about to go on the adventure of your life")
        else:
            if a == 3:
                print("Someone special is about to come into your life")
            else:
                if a == 4:
                    print("You are destined for greatness")
                else:
                    print("You can achieve everything you want")
print("Now, go spread positive vibes!")
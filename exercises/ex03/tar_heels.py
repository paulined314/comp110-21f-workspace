"""An exercise in remainders and boolean logic."""

__author__ = "730390549"


a: str = input("Enter an int: ")
b = int(a)

if (b % 14) == 0:
    print("TAR HEELS")
else:
    if (b % 2) == 0:
        print("TAR")
    else:
        if (b % 7) == 0:
            print("HEELS")
        else:
            print("CAROLINA")
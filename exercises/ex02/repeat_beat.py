"""Repeating a beat in a loop."""

__author__ = "730390549"


beat: str = input("What beat do you want to repeat? ")
inputNum: str = input("How many times do you want to repeat it? ")
repeat = int(inputNum)
if repeat <= 0:
    print("No beat...")
else:
    print((beat + " ") * (int(repeat - 1)) + beat)
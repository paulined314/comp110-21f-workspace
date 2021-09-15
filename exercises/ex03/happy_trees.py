"""Drawing forests in a loop."""

__author__ = "730390549"

Tree: str = '\U0001F332'
depth: str = input("Depth: ")
x = int(depth)
y = 0
while y <= x:
    if y > 0:
        print(Tree * int(y))
    y = y + 1

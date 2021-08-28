"""A program to show how numerical operators will work in Python."""

__author__= "730433970"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))

times: int = left ** right
print(str(left) + " ** " + str(right) + " is " + str(times))

div: float = left / right
print(str(left) + " / " + str(right) + " is " + str(div))

div_int: int = left // right
print(str(left) + " // " + str(right) + " is " + str(div_int))

remainder: float = left % right
print(str(left) + " % " + str(right) + " is " + str(remainder))
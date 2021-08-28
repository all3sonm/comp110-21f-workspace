"""A program to demonstrate how relational operators work in Python."""

__author__= "730433970"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))

less_than: bool = (left < right)
print(str(left) + " < " + str(right) + " is " + str(less_than))

at_least: bool = (left >= right)
print(str(left) + " >= " + str(right) + " is " + str(at_least))

equal_to: bool = (left == right)
print(str(left) + " == " + str(right) + " is " + str(equal_to))

not_equal_to: bool = (left != right)
print(str(left) + " != " + str(right) + " is " + str(not_equal_to))
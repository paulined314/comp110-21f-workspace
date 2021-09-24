"""polite_calculator."""
__author__ = "730390549"

input_one: str = input("Left-hand side: ")
input_two: str = input("Right-hand side: ")
math_one = int(input_one)
math_two = int(input_two)
print(str(input_one + " ** " + input_two + " is ") + str(int(math_one ** math_two)))
print(str(input_one + " / " + input_two + " is ") + str(float(math_one / math_two)))
print(str(input_one + " // " + input_two + " is ") + str(int(math_one // math_two)))
print(str(input_one + " % " + input_two + " is ") + str(int(math_one % math_two)))

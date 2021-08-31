"""polite_logic"""
_author_ = "730390549"

input_one: str = input("Left-hand side: ")
input_two: str = input("Right-hand side: ")
logic_one = int(input_one)
logic_two = int(input_two)
print(str(input_one + " < " + input_two + " is ") + str(bool(logic_one < logic_two)))
print(str(input_one + " >= " + input_two + " is ") + str(bool(logic_one >= logic_two)))
print(str(input_one + " == " + input_two + " is ") + str(bool(logic_one == logic_two)))
print(str(input_one + " != " + input_two + " is ") + str(bool(logic_one != logic_two)))
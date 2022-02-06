"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 3 Part C

In order, prompt the user for:
    1. A number (to be converted to a float)
    2. The option to do addition, subtraction, multiplication, or
    division
    3. Another number (to be converted to a float)

Print the result of the arithmetic.

Error handling:
    1. If the user selects an inappropriate operator (i.e., not
    specified in Prompt 2), state that in input is invalid.
    2. If the user attempts to divide by zero, state that such an
    operation is not possible.
    3. No other error checking
"""

print("Let's do some math.")
first_num = float(input("Enter a number, any number: "))
# print('To add, enter "+".\nTo subtract, enter"-".\nTo multiply, enter "*".\n'
#       'To divide, enter"/".')
operator = input("Enter an operator: ")
if operator not in ["+", "-", "*", "/"]:
    print("Invalid operator")
else:
    second_num = float(input("Enter another number, any number: "))
    if second_num == 0 and operator == "/":
        print("One does not simply divide by zero.")
    else:
        if operator == "+":
            print("The result is", first_num + second_num)
        if operator == "-":
            print("The result is", first_num - second_num)
        if operator == "*":
            print("The result is", first_num * second_num)
        if operator == "/":
            print("The result is", first_num / second_num)

# All work and no play makes Jack a dull boy.

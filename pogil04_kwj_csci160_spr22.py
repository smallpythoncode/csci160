"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
POGIL Activity 04

Refer to Lab 04 - Spring 2022 - Nested Loops for instructions
"""

# Instructions explicitly state not to test user input
print("Question 2.a.")
rect_width = int(input("Enter the width of the box between 1 and 10: "))
for col in range(0, rect_width):
    print("*", end=" ")

print("\nQuestion 2.b.")
rect_width = int(input("Enter the width of the box between 1 and 10: "))
rect_height = int(input("Enter the height of the box between 1 and 10: "))
for row in range(0, rect_height):
    for col in range(0, rect_width):
        print("*", end=" ")
    print()

print("\nQuestion 2.c.")
rect_width = int(input("Enter the width of the box between 1 and 10: "))
rect_height = int(input("Enter the height of the box between 1 and 10: "))
for row in range(0, rect_height):
    for col in range(0, rect_width):
        print(row + 1, end=" ")
    print()





# All work and no play makes Jack a dull boy.

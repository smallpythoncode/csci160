"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
POGIL Activity 04

Refer to Lab 04 - Spring 2022 - Nested Loops for instructions

This file contains code to answer Part 1, Questions 2.a,. 2.b., 2.c.,
and 4. It also contains code to answer part 2.

Part 1, Questions 1 and 3 are answered on the .pdf submission, but
Question 3 is included in code for reference
"""

# Instructions explicitly state not to test user input
print("Part 1, Question 2.a.")
rect_width = int(input("Enter the width of the box between 1 and 10: "))
for col in range(rect_width):
    print("*", end=" ")
print()

print("\nPart 1, Question 2.b.")
rect_width = int(input("Enter the width of the box between 1 and 10: "))
rect_height = int(input("Enter the height of the box between 1 and 10: "))
for row in range(rect_height):
    for col in range(rect_width):
        print("*", end=" ")
    print()

print("\nPart 1, Question 2.c.")
rect_width = int(input("Enter the width of the box between 1 and 10: "))
rect_height = int(input("Enter the height of the box between 1 and 10: "))
for row in range(rect_height):
    for col in range(rect_width):
        print(row + 1, end=" ")
    print()

print("\nPart 1, Question 3.")
height = 5
print("Enter height:", height)
for row in range(1, height + 1):
    for col in range(row):
        print(row, end=" ")
    print()

print("\nPart 1, Question 4.")
num = 5
print("Enter number:", num)
for row in range(num, 0, -1):
    for col in range(row):
        print(col + 1, end=" ")
    print()





# All work and no play makes Jack a dull boy.

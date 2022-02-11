"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
POGIL Activity 04

Refer to Lab 04 - Spring 2022 - Nested Loops for instructions

This file contains code to answer Part 1, Questions 2.a,. 2.b., 2.c.,
and 4. It also contains code to answer part 2.

Part 1, Questions 1 and 3 are answered on the .pdf submission.
Question 3 is included as commented code for reference.
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

# print("\nPart 1, Question 3.")
# # per instructions, height is assumed to be 5
# height = 5
# print("Enter height:", height)
# for row in range(1, height + 1):
#     for col in range(row):
#         print(row, end=" ")
#     print()

print("\nPart 1, Question 4.")
num = int(input("Enter a number: "))
for row in range(num, 0, -1):
    for col in range(row):
        print(col + 1, end=" ")
    print()

print("\nPart 1, Question 5.")
num_students = 0
while num_students < 3:
    student = input(f"Enter name of Student {num_students + 1}: ").title()
    scores = []
    while len(scores) < 3:
        try:
            score = float(input(f"Enter score of Quiz {len(scores) + 1}: "))
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("The score must be between 0 and 100.")
        except ValueError:
            print("The score must be entered as a number.")
    print(f"Name: {student}")
    print(f"Average: {sum(scores) / len(scores):.2f}\n")
    num_students += 1

print("Part 2")
print("Enter \"999\" to exit.")



# All work and no play makes Jack a dull boy.

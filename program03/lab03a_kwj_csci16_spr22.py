"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 3 Part A

Prompt the user for three inputs:
    1. A year
    2. The number of credits the student has passed
    3. The student's grade point average (GPA)

After each prompt, generate a respective output:
    1. The year is or is not within the range of 2000 to 2029 inclusive
    2. The student's undergraduate classification
    3. A description of the student's GPA

Finally, declare whether the student eligible for to graduate based on
GPA and credits passed.
"""

# prompt_1
while True:
    try:
        year = int(input("Enter a year: "))
    except ValueError:
        print("Enter year as an integer.\n")
    else:
        break

if 2000 <= year <= 2029:
    print(f"{year} is within the range of 2000 to 2029.")
else:
    print(f"{year} is not within the range of 2000 to 2029.")

# prompt_2
while True:
    try:
        num_credits = int(input("Enter the number or credits you have "
                                "passed: "))
    except ValueError:
        print("Enter year as an integer.\n")
    else:
        while num_credits < 0:
            print("It is not possible to have less than zero credits.")
        break

# if num_credits < 0:


# All work and no play makes Jack a dull boy.

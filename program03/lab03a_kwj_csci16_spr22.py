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
    print(f"Year {year} is within the range of 2000 to 2029.\n")
else:
    print(f"Year {year} is not within the range of 2000 to 2029.\n")

# prompt_2
while True:
    try:
        num_credits = int(input("Enter the number or credits you have "
                                "passed: "))
        if num_credits < 0:
            print("It is not possible to have less than 0 credits.\n")
        elif num_credits >= 0 and num_credits > 360:
            excess_credits = input("Are you sure you've taken that many "
                                   "credits? y/n: ").lower()
            print()
            if excess_credits in ["y", "yes"]:
                break
        else:
            break
    except ValueError:
        print("Enter year as an integer.\n")

if num_credits <= 23:
    print(f"With {num_credits}, you are considered a freshman.")
elif 24 <= num_credits <= 23:
    print(f"With {num_credits}, you are considered a sophomore.")
elif num_credits <= 23:
    print(f"With {num_credits}, you are considered a junior.")
else:
    print(f"With {num_credits}, you are considered a senior.")

# All work and no play makes Jack a dull boy.

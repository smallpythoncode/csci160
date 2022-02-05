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


def graduation_eligibility():
    # prompt_1
    # part of assignment, doesn't relate to eligibility
    while True:
        try:
            year = int(input("Enter a year: "))
        except ValueError:
            print("Enter year as an integer.")
        else:
            break

    if 2000 <= year <= 2029:
        print(f"Year {year} is within the range of 2000 to 2029.")
    else:
        print(f"Year {year} is not within the range of 2000 to 2029.")

    # prompt_2
    while True:
        try:
            num_credits = int(input("Enter the number or credits you have "
                                    "passed: "))
            if num_credits < 0:
                print("It is not possible to have less than 0 credits.")
            # 120 is for graduation; i'll have at least 218 by graduation
            # over 300 seems ridiculous given the context, so test created
            elif num_credits > 300:
                excess_credits = input("Are you sure you've taken that many "
                                       "credits? y/n: ").lower()
                if excess_credits in ["y", "yes"]:
                    break
            else:
                break
        except ValueError:
            print("Enter number of credits as an integer.")

    if num_credits <= 23:
        print(f"With {num_credits} credits, you are considered a freshman.")
    elif 24 <= num_credits <= 59:
        print(f"With {num_credits} credits, you are considered a sophomore.")
    elif 60 <= num_credits <= 89:
        print(f"With {num_credits} credits, you are considered a junior.")
    else:
        print(f"With {num_credits} credits, you are considered a senior.")

    # prompt_3
    while True:
        try:
            gpa = float(input("Enter your GPA: "))
            if gpa < 0:
                print("It is not possible to have a negative GPA.")
            elif gpa > 4:
                print("It is not possible to have a GPA higher than 4.000 at "
                      "UND.")
            else:
                break
        except ValueError:
            print("Enter GPA as a floating point number.")

    if gpa < 2:
        print(f"A GPA of {gpa:.3f} is POOR.")
    elif 2 <= gpa < 2.5:
        print(f"A GPA of {gpa:.3f} is SATISFACTORY")
    elif 2.5 <= gpa < 2.8:
        print(f"A GPA of {gpa:.3f} is AVERAGE.")
    elif 2.8 <= gpa < 3.2:
        print(f"A GPA of {gpa:.3f} is ABOVE AVERAGE")
    elif 3.2 <= gpa < 3.75:
        print(f"A GPA of {gpa:.3f} is GOOD")
    elif 3.75 <= gpa < 4:
        print(f"A GPA of {gpa:.3f} is VERY GOOD")
    else:
        print(f"A GPA of {gpa:.3f} is EXCELLENT")

    # eligibility statement
    if gpa >= 2.5 and num_credits >= 120:
        print("Congratulations! You are eligible to graduate!")
    else:
        print("Sorry, you are not eligible to graduate at this time.")
        if num_credits < 120:
            print(f"You need {120 - num_credits} more credits.")
        if gpa < 2.5:
            print(f"You need to improve you GPA by {2.5 - gpa:.3f}.")


if __name__ == "__main__":
    active = True
    while active:
        graduation_eligibility()
        while True:
            run_again = input("Would you like to check graduation "
                              "eligibility again? y/n: ").lower()
            if run_again not in ["y", "yes", "n", "no"]:
                print("That input was not valid.")
            elif run_again in ["n", "no"]:
                active = False
                break
            else:
                break
    print("Goodbye!")

# All work and no play makes Jack a dull boy.

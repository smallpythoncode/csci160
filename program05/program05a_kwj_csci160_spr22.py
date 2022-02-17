"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Program 05, Parts A

Determine the user's GPA this semester by:
1. Prompting for the number of classes taken.
2. For each class, prompt the user for the class name, how many credits
   the class is worth (attempted credits), and the letter grade
   received.
3. Assign the user a number of honor points determined by the letter
   grade received: 4 for an A, 3 for a B, 2 for a C, 1 for a D, and 0
   for an F.
4. Divide the number of honor points by the number of attempted credits
   to determine the GPA. Truncate this value to 4 decimal places.

Output:
1. GPA
2. Number of attempted credits
3. Number of credits passed (any letter grade other than F)
4. Number of classes attempted
5. Number of classes passed (any letter grade other than F)

Assumptions:
- All data entered will be valid (i.e., no error checking is required).
- No letter grade other than A, B, C, D, or F will be entered (upper
  case).
- If no GPA can be calculated (e.g., ZeroDivisionError), do not generate
  any output, simply end the program.
"""

total_credits_attempted = 0
credits_passed = 0
classes_attempted = int(input("Enter the number of classes this semester: "))
classes_passed = 0
honor_points = 0

# if classes_attempted < 1:
#     print("Then why are you even running this program?")
# per third assumption
if classes_attempted > 0:
    times_class_info_entered = 0
    while times_class_info_entered < classes_attempted:
        class_name = input("Enter course ID of class number "
                           f"{times_class_info_entered + 1}: ").upper()
        class_credits_attempted = int(input("Enter number of credits"
                                            f" {class_name} is worth: "))
        total_credits_attempted += class_credits_attempted
        class_letter_grade = input(f"Enter grade received for {class_name}: "
                                   ).upper()
        if class_letter_grade in ["A", "B", "C", "D"]:
            classes_passed += 1
            credits_passed += class_credits_attempted
        if class_letter_grade == "A":
            honor_points += 4 * class_credits_attempted
        if class_letter_grade == "B":
            honor_points += 3 * class_credits_attempted
        if class_letter_grade == "C":
            honor_points += 2 * class_credits_attempted
        if class_letter_grade == "D":
            honor_points += class_credits_attempted
        times_class_info_entered += 1
        print()

# per third assumption
try:
    print(format("GPA:", "18s"),
          f"{honor_points / total_credits_attempted:.4f}")
    print("Credits attempted:", f"{total_credits_attempted:6d}")
    print(format("Credits passed", "18s"), f"{credits_passed:6d}")
    print("Classes attempted:", f"{classes_attempted:6d}")
    print(format("Classes passed", "18s"), f"{classes_passed:6d}")
except ZeroDivisionError:
    pass
# address assumption 3 with while loop avoiding ZeroDivisionError

# All work and no play makes Jack a dull boy.

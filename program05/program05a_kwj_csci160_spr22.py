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
- If no GPA can be calculated (i.e, num_attempted_credits == 0), do not
  generate any output, simply end the program.
"""

num_classes = int(input("Enter the number of classes this semeter: "))
times_class_info_entered = 0
attempted_credits = 0

if num_classes != 0:
    while times_class_info_entered < num_classes:
        class_name = input("Enter course ID of class number "
                           f"{times_class_info_entered + 1}: ")
        attempted_credits += int(input(f"Enter number of credits {class_name} "
                                       "is worth: "))
        print(attempted_credits)

# All work and no play makes Jack a dull boy.

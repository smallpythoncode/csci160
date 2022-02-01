percent = round(float(input("Enter class percentage: ")), 2)
while percent < 0 or percent > 100:
    percent = float(input("Enter class percentage (range 0 to 100, "
                          "inclusive): "))

# advantage: the grade scale may change, thus, a single variable must be
# changed rather than 4 lines of code
grade_scale = {"A": 90, "B": 80, "C": 70, "D": 60}
grade = "F"
if percent >= grade_scale["A"]:
    grade = "A"
elif percent >= grade_scale["B"]:
    grade = "B"
elif percent >= grade_scale["C"]:
    grade = "C"
elif percent >= grade_scale["D"]:
    grade = "D"

print(f"A class percentage of {percent:.2f} results in a grade of {grade}.")

# All work and no play makes Jack a dull boy.

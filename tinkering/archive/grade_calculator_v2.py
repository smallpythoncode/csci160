# look for document "algorithms for common patterns" posted to blackboard

# guidelines for pass/fail (sat/unsat)
# A, B, C is pass
# D, F is fail

percent = round(float(input("Enter class percentage: ")), 2)
while percent < 0 or percent > 100:
    percent = float(input("Enter class percentage (range 0 to 100, "
                          "inclusive): "))

# passed_class = percent >= 70

if percent >= 70:
    passed_class = True
    if percent >= 90:
        grade = "A"
    elif percent >= 80:
        grade = "B"
    else:
        grade = "C"
else:
    passed_class = False
    if percent >= 60:
        grade = "D"
    else:
        grade = "F"
    # passed_class = False

print("Letter grade:", grade)
if passed_class:
    print("Passed class")
else:
    print("Failed class")

# advantage: the grade scale may change, thus, a single variable must be
# changed rather than 4 lines of code
# grade_scale = {"A": 90, "B": 80, "C": 70, "D": 60}


print(f"A class percentage of {percent:.2f} results in a grade of {grade}.")

# All work and no play makes Jack a dull boy.

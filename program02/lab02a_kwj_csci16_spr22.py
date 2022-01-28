from simple_graphics.SimpleGraphics import *


# for personal use
my_credits_needed = {
    "csci_core": 44,
    "other_depts": 17,
    "stats": 3,
    "science": 8,
    "csci_elective": 12,
    "worldviews": 3,
    "csci_capstone": 3
}

credits_graduation = 120

# for personal use
credits_current = credits_graduation - sum(my_credits_needed.values())
credits_semester = 4

# for project02 (directed to use input)
# credits_current = int(input("How many credits have you taken so far?\n\t"))
# credits_semester = int(input("How many credits are you taking this "
#                              "semester\n\t"))

print("You have completed", credits_current, "credits so far.")
print("You will have completed", credits_current + credits_semester, "credits "
      "after this semester.")
print("You have to complete", credits_graduation - credits_current, "more "
      "credits to graduate.")

# setup
setBackground("ivory")
setSize(600, 600)
setWindowTitle("Progress Towards Graduation")

# legend
setFill("dark orange")


setFill("dark orange")


setFill("dark orange")
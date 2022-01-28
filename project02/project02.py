from simple_graphics.SimpleGraphics import *


my_credits_needed = {
    "csci_core": 44,
    "other_depts": 17,
    "stats": 3,
    "science": 8,
    "csci_elective": 12,
    "worldviews": 3,
    "csci_capstone": 3
}

# num_credits_taken = int(input("How many credits have you taken so far?\n\t"))
# num_credits_this_semester = int(input("How many credits are you taking this "
#                                       "semester?"))
# num_credits_for_graduation =

credits_graduation = 120
credits_current = credits_graduation - sum(my_credits_needed.values())
credits_semester = 4

print("You have completed", credits_current, "credits so far.")
print("You will have completed", credits_current + credits_semester, "credits "
      "after this semester.")
print("You have to complete", credits_graduation - credits_current, "more "
      "credits to graduate.")

setBackground("ivory")
setSize(600, 600)
setWindowTitle("Progress Towards Graduation")

# legend
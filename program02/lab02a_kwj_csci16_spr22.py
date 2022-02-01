"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 2 Part A

Prompt for:
    1. The amount of credits the user has completed so far
    2. The amount of credits user is taking this semester
Credits needed to graduate is 120.

Print to the display:
    1. The amount of credits the user has completed so far
    2. The amount of credits the user will have completed after this
    semester
    3. The number of credits the user will need to complete after this
    semester

Using SimpleGraphics, create a bar chart with a legend that
graphically depicts the number of credits completed, taking this
semester, and needed as a percentage of the width of Tkinter display
window.
"""

from simple_graphics.SimpleGraphics import *


# for personal use
personal_credits_needed = {
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
# credits_current = credits_graduation - sum(personal_credits_needed.values())
# credits_semester = 4
# credits_needed = credits_graduation - credits_current - credits_semester

# for class assignment (directed to use input)
credits_current = int(input("How many credits have you taken so far?\n\t"))
credits_semester = int(input("How many credits are you taking this "
                             "semester\n\t"))
credits_needed = credits_graduation - credits_current - credits_semester

print("You have completed", credits_current, "credits so far.")
print("You will have completed", credits_current + credits_semester, "credits "
      "after this semester.")
print("You have to complete", credits_needed, "more credits after this "
      "semester to graduate.")

# setup
setBackground("ivory")
setSize(600, 500)
setWindowTitle("Progress Towards Graduation")

# legend
setFill("green")
rect(50, 50, 50, 50)
showText(125, 75, "Credits taken so far")
setFill("dark orange")
rect(50, 125, 50, 50)
showText(125, 150, "Credits taking this semester")
setFill("dark magenta")
rect(50, 200, 50, 50)
showText(125, 225, "Credits needed after this semester to graduate")

# bar chart
setFill("green")
width_current = (credits_current / credits_graduation) * getWidth()
rect(0, 300, width_current, 100)
showText(width_current / 2, 350, credits_current, "center")
setFill("dark orange")
width_semester = (credits_semester / credits_graduation) * getWidth()
rect(width_current, 300, width_semester, 100)
showText(width_current + width_semester / 2, 350, credits_semester, "center")
setFill("dark magenta")
width_needed = (credits_needed / credits_graduation) * getWidth()
rect(width_current + width_semester, 300, width_needed, 100)
showText(getWidth() - width_needed / 2, 350, credits_needed, "center")

# All work and no play makes Jack a dull boy.

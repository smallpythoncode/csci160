"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Project 01

Simulate a survey asking users for their major. Track the number of
Computer Science, Data Science, and Cyber Security majors. All other
majors are are tracked collectively. Accept inputs for majors until
"done" is input in the prompt.

If the user is a computer science major, prompt him/her for their minor
(if any). Minors to be tracked are Data Science, Cyber Security, and
Mathematics. All other minors and the absences of a minor are tracked
collectively.

After all data is entered, display two tables:
1. The number of students in each tracked major and the collective other
   majors, as well as the percentage for each major.
2. The number of students in each tracked minor and the collective other
   minors/absences of mines, as well as the percentage for each minor.

DEV NOTE
One minor improvement on this program could be to have a list of all the
majors offered by UND. This would be beneficial if the scope of the
survey were to track the percentages of all majors. If the user enters a
major that is not in the list, it could prompt the user to correct
his/her input. This, of course, is susceptible to innocent data entry
errors (e.g., entering "History" as "Hitsory"), thus, an expansion of
this improvement could be to implement the survey as a GUI (e.g.,
Tkinter) in which the user can select their major from a fixed list.
"""

# All work and no play makes Jack a dull boy.

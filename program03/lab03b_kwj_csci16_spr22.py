"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 3 Part B

Prompt the user for an x and y coordinate.
Repeat the coordinates back to the user using standard point notation
and declare what Cartesian coordinate quadrant the point belongs to.

It's not part of the assignment, but I am going to declare whether the
point is at the origin or along an axis. I don't like the idea of
prompting a user for information (inputting 0) then not doing anything
with it.
"""

while True:
    try:
        x_coord = float(input("Enter a value for x: "))
        y_coord = float(input("Enter a value for y: "))
    except ValueError:
        print("That is not a valid entry.")
    else:
        break

if x_coord == 0 and y_coord == 0:
    print("(0, 0) is the origin.")
elif x_coord == 0:
    print(f"(0, {y_coord:.2f}) is along the y-axis.")
elif y_coord == 0:
    print(f"({x_coord:.2f}, 0) is along the x-axis.")
elif x_coord > 0 and y_coord > 0:
    print(f"({x_coord:.2f}, {y_coord:.2f}) is in quadrant I.")
elif x_coord < 0 < y_coord:
    print(f"({x_coord:.2f}, {y_coord:.2f}) is in quadrant II.")
elif x_coord < 0 and y_coord < 0:
    print(f"({x_coord:.2f}, {y_coord:.2f}) is in quadrant III.")
else:
    print(f"({x_coord:.2f}, {y_coord:.2f}) is in quadrant IV.")

# All work and no play makes Jack a dull boy.

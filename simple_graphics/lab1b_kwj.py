"""Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 1 Part B

Using SimpleGraphics, draw a house, a sun, and a tree.
"""

from simple_graphics.SimpleGraphics import *

setSize(800, 600)
setBackground("deep sky blue")

# no matter the width of the display, the sun will be in the upper right
sun_x = getWidth() - 100

# draw sun shape
setFill("khaki")
circle(sun_x, 80, 60)
# draw sun mouth
setFill("black")
blob(sun_x - 50, 90, sun_x - 30, 110, sun_x - 10, 130, sun_x + 10, 110,
     sun_x + 30, 90)
# draw sun eyes
setFill("white")
circle(sun_x - 30, 65, 15)
circle(sun_x + 10, 55, 22)
setFill("black")
circle(sun_x - 33, 66, 8)
circle(sun_x + 5, 65, 6)

# draw grass
setFill("forest green")
rect(0, 500, getWidth(), getHeight() - 500)

# draw house shape
setFill("dark khaki")
rect(100, 300, 300, 200)
# draw roof
setFill("slate blue")
triangle(100, 300, 250, 200, 400, 300)
# draw door
setFill("saddle brown")
rect(150, 350, 75, 150)
setFill("yellow")
circle(160, 425, 7)
# draw windows
setFill("deep sky blue")
rect(275, 350, 35, 35)
rect(310, 350, 35, 35)
rect(275, 385, 35, 35)
rect(310, 385, 35, 35)

# draw "A TREE"
setOutline("firebrick")
setLineWidth(10)
# "A"
line(575, 300, 600, 350)
line(575, 300, 550, 350)
line(565, 325, 585, 325)
# y-axis reference points for "TREE"
tree_top = 400
tree_bottom = 450
# "T"
line(500, tree_top, 500, tree_bottom)
line(475, tree_top, 525, tree_top)
# "R"
line(550, tree_top, 550, tree_bottom)
line(550, tree_top, 575, tree_top + 12)
line(550, tree_top + 25, 575, tree_top + 12)
line(550, tree_top + 25, 575, tree_bottom)
# reference point for first "E" along x-axis
e1_x = 600
line(e1_x, tree_top, e1_x, tree_bottom)
line(e1_x, tree_top, e1_x + 25, tree_top)
line(e1_x, tree_top + 25, e1_x + 25, tree_top + 25)
line(e1_x, tree_bottom, e1_x + 25, tree_bottom)
# reference point for second "E" along x-axis
e2_x = e1_x + 50
line(e2_x, tree_top, e2_x, tree_bottom)
line(e2_x, tree_top, e2_x + 25, tree_top)
line(e2_x, tree_top + 25, e2_x + 25, tree_top + 25)
line(e2_x, tree_bottom, e2_x + 25, tree_bottom)

# All work and no play makes Jack a dull boy.

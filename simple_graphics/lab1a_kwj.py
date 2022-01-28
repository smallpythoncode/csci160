"""Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 1 Part A

Using SimpleGraphics, draw a face with a minimum of 2 eyes, 1 nose,
and 1 mouth.
"""

from simple_graphics.SimpleGraphics import *

setSize(400, 300)
setBackground("hot pink")

# no matter the width of the display, the face is centered along the x-axis
sun_x = getWidth() / 2

# draw head
setFill("lime")
ellipse(sun_x, 80, 80, 60)

# draw mouth
setFill("black")
blob(sun_x - 50, 90, sun_x - 30, 110, sun_x - 10, 130, sun_x + 10, 110,
     sun_x + 30, 90)

# draw eyes
setFill("deep sky blue")
circle(sun_x - 50, 65, 15)
circle(sun_x + 30, 55, 22)
setFill("indigo")
circle(sun_x - 53, 66, 8)
circle(sun_x + 25, 65, 6)

# draw nose
setLineWidth(5)
line(sun_x - 10, 60, sun_x - 20, 70)
line(sun_x - 10, 80, sun_x - 20, 70)

# All work and no play makes Jack a dull boy.

"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Program 05, Part B

Use SimpleGraphics to draw your initials. To ensure practice of loops,
only the point command can be used to draw.
"""

from simple_graphics.SimpleGraphics import *


setSize(400, 150)
setBackground("black")
setLineWidth(5)
setOutline("lime green")

# start of letter "K"
start_x_k = 25
start_y_k = 25
half_y_k = start_y_k + 50

for y_dot in range(0, 100):
    point(start_x_k, start_y_k + y_dot)

line2_x_k = start_x_k
for y_dot in range(0, 50):
    for x_dot in range(0, 2):
        point(line2_x_k + x_dot, half_y_k + y_dot)
    line2_x_k += 2

line3_x_k = start_x_k
for y_dot in range(0, 50):
    for x_dot in range(0, 2):
        point(line3_x_k + x_dot, half_y_k - y_dot)
    line3_x_k += 2

# start of letter "W"
start_x_w = start_x_k + 125
start_y_w = start_y_k
q1_x_w = start_x_w + 25
half_x_w = q1_x_w + 25
q3_x_w = half_x_w + 25

line1_y_w = start_y_w
for x_dot in range(0, 25):
    for y_dot in range(0, 4):
        point(start_x_w + x_dot, line1_y_w + y_dot)
    line1_y_w += 4

line2_y_w = start_y_w + 100
for x_dot in range(0, 25):
    for y_dot in range(0, 4):
        point(q1_x_w + x_dot, line2_y_w - y_dot)
    line2_y_w -= 4

line3_y_w = start_y_w
for x_dot in range(0, 25):
    for y_dot in range(0, 4):
        point(half_x_w + x_dot, line3_y_w + y_dot)
    line3_y_w += 4

line4_y_w = start_y_w + 100
for x_dot in range(0, 25):
    for y_dot in range(0, 4):
        point(q3_x_w + x_dot, line4_y_w - y_dot)
    line4_y_w -= 4

# start of letter "W"
start_x_j = start_x_w + 125
start_y_j = start_y_w

for x_dot in range(0, 100):
    point(start_x_j + x_dot, start_y_j)

for y_dot in range(0, 100):
    point(start_x_j + 50, start_y_j + y_dot)

for x_dot in range(0, 50):
    point(start_x_j + x_dot, start_y_j + 100)

for y_dot in range(0, 25):
    point(start_x_j, start_y_j + 100 - y_dot)

# All work and no play makes Jack a dull boy.

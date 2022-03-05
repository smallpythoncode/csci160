"""
Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 06, Part B

# TODO: explain the premise
# TODO: provide explanations of functions

"""

from simple_graphics.SimpleGraphics import *


def draw_k(x, y, letter_color=None):
    if letter_color is None:
        letter_color = "lime green"
    setOutline(letter_color)
    start_x_k = x
    start_y_k = y
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


def draw_w(x, y, letter_color=None):
    if letter_color is None:
        letter_color = "peru"
    setOutline(letter_color)
    start_x_w = x
    start_y_w = y
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


def draw_j(x, y, letter_color=None):
    if letter_color is None:
        letter_color = "slate blue"
    setOutline(letter_color)
    start_x_j = x
    start_y_j = y

    for x_dot in range(0, 100):
        point(start_x_j + x_dot, start_y_j)

    for y_dot in range(0, 100):
        point(start_x_j + 50, start_y_j + y_dot)

    for x_dot in range(0, 50):
        point(start_x_j + x_dot, start_y_j + 100)

    for y_dot in range(0, 25):
        point(start_x_j, start_y_j + 100 - y_dot)


def draw_shadow_k(x, y, letter_color=None, offset=3):
    if letter_color is None:
        letter_color = "black"
    setOutline(letter_color)
    shadow_x_k = x + offset
    shadow_y_k = y + offset
    draw_k(shadow_x_k, shadow_y_k, letter_color)


def draw_shadow_w(x, y, letter_color=None, offset=3):
    if letter_color is None:
        letter_color = "black"
    setOutline(letter_color)
    shadow_x_w = x + offset
    shadow_y_w = y + offset
    draw_w(shadow_x_w, shadow_y_w, letter_color)


def draw_shadow_j(x, y, letter_color=None, offset=3):
    if letter_color is None:
        letter_color = "black"
    setOutline(letter_color)
    shadow_x_j = x + offset
    shadow_y_j = y + offset
    draw_j(shadow_x_j, shadow_y_j, letter_color)


def main():
    setSize(400, 150)
    setBackground("old lace")
    setLineWidth(5)
    current_x = 25
    current_y = 25

    draw_shadow_k(current_x, current_y)
    draw_k(current_x, current_y)
    current_x += 125

    draw_shadow_w(current_x, current_y)
    draw_w(current_x, current_y)
    current_x += 125

    draw_shadow_j(current_x, current_y)
    draw_j(current_x, current_y)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

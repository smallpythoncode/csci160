"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 06, Part B



"""

def setup(func):
    def positions_and_colors():
        color = "red"
        starting_position = 125
        func(color, starting_position)
    return positions_and_colors()

@setup
def print_k():


from simple_graphics import SimpleGraphics

# All work and no play makes Jack a dull boy.

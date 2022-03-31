"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 09, Part 2

# TODO - add description

Required Functions:

    fillListFromFile (fileName):
        Reads a file and returns a list of values from that file.
    adjustList (theList):
        # TODO - add description
    calcAverage (theList):
        Calculates the average of a list of values.
    getColor (value)
        # TODO - add description
    indexOfMaxValue (theList)
        # TODO - add description
    drawGraph (theList)
        # TODO - add description
"""

from simple_graphics.SimpleGraphics import *


def fillListFromFile (fileName):
    """Reads a file and returns a list of values from that file.

    No error checking is required.

    :param fileName: The file to be read
    :type fileName: str
    :return: A list of values from the file
    :rtype: list
    """
    valueList = []
    with open(fileName) as f:
        for value in f:
            valueList.append(int(value))

    return valueList


# TODO
def adjustList (theList):
    pass


def calcAverage (theList):
    """Calculates the average of a list of values.

    :param theList: The list of which the average is to be found.
    :type theList: list
    :return: The average of the values of theList
    :rtype: float
    """
    sum = 0
    numValues = 0
    for value in theList:
        sum += value
        numValues += 1

    return sum / numValues


# TODO
def getColor (value)
    pass


# TODO - Refer to findMaxValue() from program08
def indexOfMaxValue (theList)
    pass


# TODO
def drawGraph (theList)
    pass


# TODO - finalize
def main():
    pass


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

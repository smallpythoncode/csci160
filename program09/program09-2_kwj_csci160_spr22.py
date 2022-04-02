"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 09, Part 2

# TODO - add description

Required Functions:

    fillListFromFile (fileName):
        Reads a file and returns a list of values from that file.
    adjustList (theList):
        Modifies values in a list to ensure they are in range 0 to 100.
    calcAverage (theList):
        Calculates the average of a list of values.
    getColor (value)
        # TODO - add description
    indexOfMaxValue (theList)
        # TODO - add description
    drawGraph (theList)
        # TODO - add description
"""

# from simple_graphics.SimpleGraphics import *


def fillListFromFile (fileName):
    """Reads a file and returns a list of values from that file.

    No error checking is required. Converts floats to integers.

    :param fileName: The file to be read
    :type fileName: str
    :return: A list of values from the file
    :rtype: list
    :raise ValueError: Supports only numerical values (integers).
    """
    valueList = []
    with open(fileName) as f:
        for value in f:
            valueList.append(int(value))

    return valueList


def adjustList (theList):
    """Modifies values in a list to ensure they are in range 0 to 100.

    Designed to handle integer values. Will convert floats.

    :param theList: List of any values of no specified range
    :type theList: list
    :return: List of values with a max. of 100 and min. of 0
    :rtype: list
    :raise ValueError: Supports only numerical values (integers).
    """
    adjustedList = []
    for i in range(len(theList)):
        if theList[i] > 100:
            adjustedList.append(100)
        elif theList[i] < 0:
            adjustedList.append(0)
        else:
            adjustedList.append(theList[i])

    return adjustedList


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


def getColor (value):
    """Returns a color name dependent on value.

    :param value: The integer that determines the color
    :type value: int
    :return: The color appropriate to the integer
    :rtype: str
    """
    if 95 <= value <= 100:
        return "darkred"
    if 90 <= value <= 94:
        return "red"
    if 70 <= value <= 89:
        return "green"
    if 60 <= value <= 69:
        return "blue"
    if 0 <= value <= 59:
        return "darkblue"


# TODO - Refer to findMaxValue() from program08
def indexOfMaxValue (theList):
    pass


# TODO
def drawGraph (theList):
    pass


# TODO - finalize
def main():
    # file = input("Enter the file name: ")
    file = "values09.txt"
    originalList = fillListFromFile(file)
    adjustedList = adjustList(originalList)
    # TODO - delete print statments
    print(originalList)
    print(adjustedList)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

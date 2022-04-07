"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 09, Part 2

Create a module with the following required functions for list manipulation
and processing and for use with SimpleGraphics:

Required Functions:

    fillListFromFile (fileName):
        Reads a file and returns a list of values from that file.
    adjustList (theList):
        Copies thelist, modifies values to range 0 to 100.
    calcAverage (theList):
        Calculates the average of a list of values.
    getColor (value)
        Returns a color name dependent on value.
    indexOfMaxValue (theList)
        Finds the maximum value of theList.
    drawGraph (theList)
        Draws a bar graph for the values in theList and the average.

Discretionary Functions:

    printMaxInfo (maxInfo):
        Prints information about maximum values.
"""

from simple_graphics.SimpleGraphics import *


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
    """Copies thelist, modifies values to range 0 to 100.

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


def indexOfMaxValue (theList):
    """Finds the maximum value of theList.

    :param theList: The list in which to find the maximum
    :type theList: list
    :return: The maximum value and its indexes w/in the list
    :rtype: tuple
    """
    max_value = theList[0]
    max_index = []

    for i in range(len(theList)):
        if theList[i] == max_value:
            max_index.append(i)
        elif theList[i] > max_value:
            max_index.clear()
            max_value = theList[i]
            max_index.append(i)

    return max_value, max_index


def drawGraph (theList):
    """Draws a bar graph for the values in theList and the average.

    :param theList: The values to be displayed
    :type theList: list
    :rtype: None
    """
    setWindowTitle("There's a snake in my boot.")
    setSize(700, 500)
    setOutline("black")
    setBackground("lightgray")
    setFill("white")
    graphLeft = 50
    graphTop = 50
    graphWidth = 600
    graphHeight = 400
    rect(graphLeft, graphTop, graphWidth, graphHeight)

    barWidth = graphWidth / len(theList)
    barStart = graphLeft
    for bar in theList:
        setFill(getColor(bar))
        barHeight = graphHeight * (bar / 100)
        barTop = graphTop + (1 - barHeight) + 400
        rect(barStart, barTop, barWidth, barHeight)
        barStart += barWidth

    setLineWidth(5)
    averageLine = graphTop + (graphHeight * (1 - (calcAverage(theList) / 100)))
    line(graphLeft, averageLine, graphLeft + graphWidth, averageLine)

    numPosition = graphLeft + (barWidth / 2) - 5
    for i in range(len(theList)):
        showText(numPosition, 465, i + 1)
        numPosition += barWidth


def printMaxInfo (maxInfo):
    """Prints information about maximum values.

    :param maxInfo:
        index0 = the maximum value
        index1 = list of indexes at which the maximum appears
        (maxValue, [maxValue, at, index, list])
    :type maxInfo: tuple
    :rtype: None
    """
    print("Maximum value:", str(maxInfo[0]))
    print(f"Index(es) of max value: ", end="")
    for value in maxInfo[1][:-1]:
        print(value, end=", ")
    print(maxInfo[1][-1])


def main():
    file = input("Enter the file name: ")
    originalList = fillListFromFile(file)
    adjustedList = adjustList(originalList)
    print("Original list:", originalList)
    print("Adjusted list:", adjustedList)
    print("Average of original values:", calcAverage(originalList))
    print("Average of adjusted values:", calcAverage(adjustedList))
    maxValueInfo = indexOfMaxValue(adjustedList)
    printMaxInfo(maxValueInfo)
    drawGraph(adjustedList)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

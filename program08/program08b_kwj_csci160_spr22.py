"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program XX, Part X

# TODO description

Functions:

    # TODO write the functions
    ---REQUIRED---
    fillListFromFile (fileName):
        Reads a file and creates a list of values from that file.
    findMaxValue (theList):
        Finds the maximum value in a list.
    findMinValue (theList):
        Finds the minimum value in a list.


    ---NOT REQUIRED---

"""


def fillListFromFile (fileName):
    """Reads a file and creates a list of values from that file.

    :param fileName: The file to be read
    :type fileName: str
    :return: A list of values from the file
    :rtype: list
    """
    valueList = []
    with open(fileName) as f:
        for value in f:
            valueList.append(float(value))

    return valueList


def findMaxValue (theList):
    """Finds the maximum value in a list.

    :param theList: The list in which to find a maximum
    :type theList: list
    :return: The maximum value
    :rtype: float or int
    """
    maxValue = ""
    for value in theList:
        if maxValue == "":
            maxValue = value
        else:
            if value > maxValue:
                maxValue = value

    return maxValue


def findMinValue (theList):
    """Finds the minimum value in a list.

    :param theList: The list in which to find a minimum
    :type theList: list
    :return: The minimum value
    :rtype: float or int
    """
    minValue = ""
    for value in theList:
        if minValue == "":
            minValue = value
        else:
            if value < minValue:
                minValue = value

    return minValue


# TODO
def calcRange (theList):
    pass


# TODO
def calcAverage (theList):
    pass


# TODO
def calcGeometricMean (theList):
    pass


# TODO
def standardDeviation (theList):
    pass


# TODO
def main():
    # Instructions explicitly state to ask for file name in main().
    # Ideally, a function would be created for this, one that uses the isfile
    # method from os.path package
    # TODO remove file used for testing
    # file = input("Enter the file name: )
    file = "values.txt"

    valueList = fillListFromFile(file)
    print(valueList)
    print("Maximum value:", findMaxValue(valueList))
    print("Minimum value:", findMinValue(valueList))









if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

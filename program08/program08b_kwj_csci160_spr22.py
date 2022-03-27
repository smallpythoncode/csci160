"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 08, Part 2

Write the required functions and print the return values in the main
function. Avoid built-in methods that perform the same task.

Required Functions:

    fillListFromFile (fileName):
        Reads a file and creates a list of values from that file.
    findMaxValue (theList):
        Finds the maximum value in a list.
    findMinValue (theList):
        Finds the minimum value in a list.
    calcRange (theList):
        Calculates the range of a list of values.
    calcAverage (theList):
        Calculates the average of a list of values.
    calcGeometricMean (theList):
        Calculates the geometric mean of a list of values.
    standardDeviation (theList):
        Calculates the standard deviation for a list of values.
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
    :return: The maximum value in theList
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
    :return: The minimum value in theList
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


def calcRange (theList):
    """Calculates the range of a list of values.

    :param theList: The list in which to find the range
    :type theList: list
    :return: The range of a theList (max - min)
    :rtype: float or int
    """
    return findMaxValue(theList) - findMinValue(theList)


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


def calcGeometricMean (theList):
    """Calculates the geometric mean of a list of values.

    :param theList: The list of which the geometric mean
    :type theList: list
    :return: The geometric mean of the values of theList
    :rtype: float
    """
    product = 1
    root = 0
    for value in theList:
        product *= value
        root += 1

    return product ** (1 / root)


def standardDeviation (theList):
    """Calculates the standard deviation for a list of values.

    Utilizes the population formula for standard deviation.

    :param theList: The list of which to find the standard deviation
    :type theList: list
    :return: The standard deviation of theList
    :rtype: float
    """
    average = calcAverage(theList)
    squaredDifferencesSum = 0
    # not sample
    population = 0
    for value in theList:
        value = (value - average) ** 2
        squaredDifferencesSum += value
        population += 1

    return (squaredDifferencesSum / population) ** (1 / 2)


def main():
    # Instructions explicitly state to ask for file name in main().
    # Ideally, a function would be created for this, one that uses the isfile
    # method from os.path package
    file = input("Enter the file name: ")
    valueList = fillListFromFile(file)

    print()
    print("Maximum value:", findMaxValue(valueList))
    print("Minimum value:", findMinValue(valueList))
    print("Range:", calcRange(valueList))
    print("Average:", calcAverage(valueList))
    print("Geometric mean:", calcGeometricMean(valueList))
    print("Standard deviation:", standardDeviation(valueList))


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 11, Part 2
Copyright (C) 2022 Kenneth Jahnke

# TODO add description

.. note::
    Assignment instructions do not state built-in Python methods
    (such as sort) could not be utilized.

Required Functions:
    totalStudents (theDictionary)
        - # TODO
    matchingByName (theDictionary, firstLetter)
        - # TODO
    matchingByLocker (theDictionary, LowerLimit, upperLimit)
        - # TODO
    firstLocker (theDictionary)
        - # TODO
    lastLocker (theDictionary)
        - # TODO
    findLocker (theDictionary, studentName)
        - # TODO
    findStudent (theDictionary, lockerNum)
        - # TODO
    students (theDictionary)
        - # TODO
    printInfoSortedByStudent (title, theDictionary)
        - # TODO
    printInfoSortedByLocker (title, theDictionary)
        - # TODO

Discretionary Functions:
    promptTextFileRead ():
        - Prompts for desired text file name for use in read mode.
    lockerNumDigits (lockerNum, digits=3):
        - Adds leading zeroes to ensure len (lockerNum) == digits.
"""

from os.path import isfile


# discretionary
def promptTextFileRead ():
    """Prompts for desired text file name for use in read mode.

    :return: The name of a text file if it exists, else None
    :rtype: str or None
    """
    while True:
        fileName = input ("Text file name: ")

        if fileName == "":
            break
        elif fileName[-4:] != ".txt":
            print ("File name must include \".txt\" extension.")
        else:
            if isfile(fileName):
                return fileName
            else:
                print(fileName, "does not exist.\n"
                                "Input another text file name or press "
                                "\"Enter\" to exit.")


# discretionary
def lockerNumDigits (lockerNum, digits=3):
    """Adds leading zeroes to ensure len (lockerNum) == digits.

    :param str lockerNum:
        The locker number to ensure has sufficient digits
    :param int digits:
        The assigned number of digits for locker numbers to include
        leading zeroes
    :except ValueError:
        lockerNum must be able to be represented as an int. Returns None
        otherwise.
    :return:
        The locker number with sufficient digits unless len (lockerNum)
        > digits, then returns None
    :rtype: str or None
    """
    try:
        int (lockerNum)
    except ValueError:
        return None

    if 1 <= len (lockerNum) <= digits:
        lockerNum = "0" * (digits - len (lockerNum)) + lockerNum
        return lockerNum


# discretionary
# TODO - modify for assignment context
def readClasses (fileName):
    """Reads fileName and converts its data into a dictionary.

    Per assignment instructions, no error checking is required.

    :param str fileName: The text file name containing class data.
        Include .txt file extension.
    :return: A dictionary containing class data with the class name
        as the keys an number of credits for that class as the values.
    :rtype: dict
    """
    classInfo = {}

    with open(fileName) as f:
        for line in f:
            classesAndCredits = line.split("\t")
            # [0] strips "\n"
            classInfo[classesAndCredits[0]] = int(classesAndCredits[1][0])

    return classInfo

# TODO
def totalStudents (theDictionary):
    """
    # TODO
    :param theDictionary:
    :return:
    """



# TODO
def matchingByName (theDictionary, firstLetter):
    """
    # TODO
    :param theDictionary:
    :param firstLetter:
    :return:
    """


# TODO
def matchingByLocker (theDictionary, LowerLimit, upperLimit):
    """
    # TODO
    :param theDictionary:
    :param LowerLimit:
    :param upperLimit:
    :return:
    """
    # if lower limit, upper limit not in range of len (theDictionary)


# TODO
def firstLocker (theDictionary):
    """
    # TODO
    :return:
    """


# TODO
def lastLocker (theDictionary):
    """
    # TODO
    :param theDictionary:
    :return:
    """


# TODO
def findLocker (theDictionary, studentName):
    """
    # TODO
    :param theDictionary:
    :param studentName:
    :return:
    """


# TODO
def findStudent (theDictionary, lockerNum):
    """
    # TODO
    :param theDictionary:
    :param lockerNum:
    :return:
    """


# TODO
def students (theDictionary):
    """
    # TODO
    :param theDictionary:
    :return:
    """


# TODO
def printInfoSortedByStudent (title, theDictionary):
    """
    # TODO
    :param title:
    :param theDictionary:
    :return:
    """


# TODO
def printInfoSortedByLocker (title, theDictionary):
    """
    # TODO
    :param title:
    :param theDictionary:
    :return:
    """


def main ():
    print ("Enter name of text file containing locker assignment information.")
    lockers = promptTextFileRead ()

    if not lockers:
        print ("Locker assignment information not acquired.\nExiting program.")
    else:
        pass


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

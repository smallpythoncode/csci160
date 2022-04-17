"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program XX, Part X
Copyright (C) 2022 Kenneth Jahnke

Required Functions:

    readClasses (fileName)
        - TODO
    totalCredits (theDictionary)
        - TODO
    classesByDepartment (theDictionary, department)
        - TODO
    classesByCredits (theDictionary, credtits)
        - TODO
    isFulltime (theDictionary)
        - TODO
    numOfClasses (theDictionary)
        - Returns the number of classes a student is taking.
    upperLevelCredits (theDictionary)
        - TODO
    printClasses (theDictionary)
        - TODO

Discretionary Functions:

    promptFileNameRead ()
        - Prompts for desired text file name for use in read mode.

    # TODO
"""
from os.path import isfile


# discretionary
def promptFileNameRead ():
    """Prompts for desired text file name for use in read mode.

    Designed to use in conjunction with reading of files. Returns name
    of text file if it exists, otherwise None.

    :return: The name of a .txt file
    :rtype: str
    """
    while True:
        fileName = input ("Enter desired text file name. Do not add a file "
                         "extension.\nFile name: ")

        if fileName == "":
            break
        else:
            fileName = fileName + ".txt"
            if isfile(fileName):
                return fileName
            else:
                print(fileName, "does not exist.\n"
                                "Input another file name or press "
                                "\"Enter\" to exit.")


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


def totalCredits (theDictionary):
    """Calculates the total credits the student is taking this semester.

    :param dict theDictionary: The student's class information
    :return: The total credits
    :rtype: int
    """
    total = 0  # = sum (theDictionary.values ())

    for i in theDictionary:
        total += theDictionary[i]

    return total


def classesByDepartment (theDictionary, department):
    """Lists the courses being taken from specific department.

    :param dict theDictionary: The student's class information
    :param str department: The department in question
    :return: The courses being taken within department
    :rtype: list
    """
    department = department.upper ().strip ()
    classes = []

    for i in theDictionary:
        classDept = i.split ()[0]
        if classDept == department:
            classes.append (i)

    return classes


def classesByCredits (theDictionary, credits):
    """Lists the courses worth a specific credit value.

    :param dict theDictionary: The student's class information
    :param int credits: The credit value by which classes are queried
    :return: The courses worth the value of credits
    :rtype: list
    """
    classes = []

    for i in theDictionary:
        if theDictionary[i] == credits:
            classes.append(i)

    return classes


# TODO
# TODO utilize totalCredits ()
def isFulltime (theDictionary):
    """
    TODO
    :param dict theDictionary: The student's class information
    :return:
    """
    pass


# TODO test this
def numOfClasses (theDictionary):
    """Returns the number of classes a student is taking.

    .. note::
        Does not couple labs to classes. BIOL 150 and BIOL 150L are
        counted as separate classes.

    :param dict theDictionary: The student's class information
    :return: The number of classes
    :rtype: int
    """
    return len (theDictionary)


# TODO
def upperLevelCredits (theDictionary):
    """
    TODO
    :param dict theDictionary: The student's class information
    :return:
    """
    pass


# TODO
def printClasses (theDictionary):
    """
    TODO
    :param dict theDictionary: The student's class information
    :return:
    """
    pass


def main ():
    print ("This program will read class data from a text file then give us "
           "information about that data.")
    # FIXME
    # fileName = promptFileNameRead()
    small = "small.txt"
    big = "big.txt"
    fileName = big

    if fileName is None:
        print ("No valid file name passed. Exiting program.")
    else:
        classInfo = readClasses (fileName)
        print (classInfo)
        numTotalCredits = totalCredits (classInfo)
        print ("Total number of credits:", numTotalCredits)
        computerScience = "CSCI"
        listOfCSCICourses = classesByDepartment (classInfo, computerScience)
        print (computerScience, "courses:", listOfCSCICourses)
        numCreditQuery = 3
        listOf3CreditCourses = classesByCredits (classInfo, numCreditQuery)
        print (numCreditQuery, "-credit courses: ", listOf3CreditCourses,
               sep="")










if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

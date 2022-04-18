"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 10, Part 2
Copyright (C) 2022 Kenneth Jahnke

Required Functions:

    readClasses (fileName)
        - Reads fileName and converts its data into a dictionary.
    totalCredits (theDictionary)
        - Calculates the total credits student is taking this semester.
    classesByDepartment (theDictionary, department)
        - Lists the courses being taken from specific department.
    classesByCredits (theDictionary, credits)
        - Lists the courses worth a specific credit value.
    isFulltime (theDictionary)
        - Determines if student is full-time (>= 12 credits).
    numOfClasses (theDictionary)
        - Returns the number of classes a student is taking.
    upperLevelCredits (theDictionary)
        - Counts the number of upper-level undergraduate credits.
    printClasses (theDictionary)
        - Prints a table displaying the student's class information.

Discretionary Functions:

    promptFileNameRead ()
        - Prompts for desired text file name for use in read mode.
    listSortAscending (listToSort):
        - Sorts the contents of a list in ascending order.
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


# discretionary
def listSortAscending (listToSort):
    """Sorts the contents of a list in ascending order.

    :param list listToSort: The items to be sorted.
    :raise TypeError: listToSort must be comprised of objects of like
        types; cannot compare strings to ints/floats
    :rtype: None
    """
    # this index...
    for targetIndex in range (0, len (listToSort) - 1):
        # ...compared to this index
        for comparisonIndex in range (targetIndex + 1, len (listToSort)):
            if listToSort[targetIndex] > listToSort[comparisonIndex]:
                # target character
                temp = listToSort[comparisonIndex]
                # character moved into unsorted series
                listToSort[comparisonIndex] = listToSort[targetIndex]
                # target character moved into sorted position
                listToSort[targetIndex] = temp


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
    """Calculates the total credits student is taking this semester.

    :param dict[str, int] theDictionary: The student's class information
        with the class as the key and the number or credits as the value
    :return: The total credits
    :rtype: int
    """
    total = 0  # = sum (theDictionary.values ())

    for i in theDictionary:
        total += theDictionary[i]

    return total


def classesByDepartment (theDictionary, department):
    """Lists the courses being taken from specific department.

    :param dict[str, int] theDictionary: The student's class information
        with the class as the key and the number or credits as the value
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

    :param dict[str, int] theDictionary: The student's class information
        with the class as the key and the number or credits as the value
    :param int credits: The credit value by which classes are queried
    :return: The courses worth the value of credits
    :rtype: list
    """
    classes = []

    for i in theDictionary:
        if theDictionary[i] == credits:
            classes.append(i)

    return classes


def isFulltime (theDictionary):
    """Determines if student is full-time (>= 12 credits).

    :param dict[str, int] theDictionary: The student's class information
        with the class as the key and the number or credits as the value
    :return: True if full-time, False otherwise
    :rtype: bool
    """
    total = totalCredits(theDictionary)
    if total >= 12:
        return True
    else:
        return False


def numOfClasses (theDictionary):
    """Returns the number of classes a student is taking.

    .. note::
        Does not couple labs to classes. For instance, BIOL 150 and BIOL
        150L are counted as separate classes.

    :param dict[str, int] theDictionary: The student's class information
        with the class as the key and the number or credits as the value
    :return: The number of classes
    :rtype: int
    """
    return len (theDictionary)


def upperLevelCredits (theDictionary):
    """Counts the number of upper-level undergraduate credits.

    :param dict[str, int] theDictionary: The student's class information
        with the class as the key and the number or credits as the value
    :return: The number of credits
    :rtype: int
    """
    numCredits = 0

    for i in theDictionary:
        deptAndNum = i.split ()
        if int (deptAndNum[1][:3]) in range(300, 500):
            numCredits += theDictionary[i]

    return numCredits


def printClasses (theDictionary):
    """Prints a table displaying the student's class information.

    List classes alphabetically in the left column, their credit-worth
    in the right column. The last row displays the total number of
    credits.

    :param dict[str, int] theDictionary: The student's class information
        with the class as the key and the number or credits as the value
    :rtype: None
    """
    classes = [i for i in theDictionary]
    listSortAscending (classes)

    print ("CLASS NAME    | CREDITS")
    print ("=" * 23)
    for className in classes:
        print (f"{className:<13s}", "|", f"{theDictionary[className]:>7d}")
    print ("=" * 23)
    print (f"TOTAL CREDITS | {totalCredits (theDictionary):>7d}")


def main ():
    print ("This program will read class data from a text file then give us "
           "information about that data.\n")
    fileName = promptFileNameRead()

    if fileName is None:
        print ("No valid file name passed. Exiting program.")
    else:
        # readClasses test
        classInfo = readClasses (fileName)
        print("The dictionary containing class information:\n\t", classInfo)

        # totalCredits test
        print ("Total number of credits:", totalCredits (classInfo))

        # classesByDepartment test
        departmentQuery = "CSCI"
        listOfCSCICourses = classesByDepartment (classInfo, departmentQuery)
        print (departmentQuery, "courses:", listOfCSCICourses)

        # classesByCredits test
        numCreditQuery = 3
        listOf3CreditCourses = classesByCredits (classInfo, numCreditQuery)
        print (numCreditQuery, "-credit courses: ", listOf3CreditCourses,
               sep="")

        # isFullTime test
        print ("Student is full-time:", isFulltime (classInfo))

        # numOfClasses test
        print ("Number of classes:", numOfClasses (classInfo))

        # upperLevelCredits test
        print ("Number of upper-level credits:", upperLevelCredits(classInfo))

        # printClasses test
        print ()
        printClasses (classInfo)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

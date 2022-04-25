"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 11, Part 2
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    1. Prompt user for a file containing locker assignment data.
    2. Store that data to a dictionary.
    3. Write the required data exploitation functions.

.. note::
    Function HEADERS written exactly as specified in instructions.
.. note::
    Locker numbers are presumed to be strings representing a 3-digit
    locker number. Lockers without a student assignment have a value of
    "open".

Required Functions:
    totalStudents (theDictionary)
        - Identifies the total number of students assigned a locker.
    matchingByName (theDictionary, firstLetter)
        - Identifies students a name starting with firstLetter.
    matchingByLocker (theDictionary, LowerLimit, upperLimit)
        - Identifies students with lockers within a locker number range.
    firstLocker (theDictionary)
        - Identifies the first locker number.
    lastLocker (theDictionary)
        - Identifies the last locker number.
    findLocker (theDictionary, studentName)
        - Finds the locker(s) assigned to studentName.
    findStudent (theDictionary, lockerNum)
        - Identifies what student is assigned to lockerNum, if any.
    students (theDictionary)
        - Identifies students with a locker and sorts them into a list.
    printInfoSortedByStudent (title, theDictionary)
        - Prints locker assignment data sorted by student.
    printInfoSortedByLocker (title, theDictionary)
        - Prints locker assignment data sorted by locker.

Discretionary Functions:
    promptTextFileRead ():
        - Prompts for desired text file name for use in read mode.
    lockerNumDigits (lockerNum, theDictionary):
        - Adds leading zeroes as needed to lockerNum.
    textFileToDict (fileName, delimiter="\t"):
        - Reads fileName and converts its data into a dictionary.
"""

from os.path import isfile


# discretionary
def promptTextFileRead ():
    """Prompts for desired text file name for use in read mode.

    :return: The name of a text file if it exists, else None
    :rtype: str or None
    """
    while True:
        fileName = input("Text file name: ")

        if fileName == "":
            break
        elif fileName[-4:] != ".txt":
            print("File name must include \".txt\" extension.")
        else:
            if isfile(fileName):
                return fileName
            else:
                print(fileName, "does not exist.\nInput another text "
                                "file name or press \"Enter\" to exit.")


# discretionary
def lockerNumDigits (lockerNum, theDictionary):
    """Adds leading zeroes as needed to lockerNum.

    End number of digits of lockerNum (leading zeroes and the num) is
    equivalent to number of digits of length of theDictionary.

    :param str lockerNum:
        The locker number to ensure has sufficient digits
    :param dict theDictionary:
        The length of theDictionary determines the total number of
        digits.
    :except ValueError:
        lockerNum must be able to be represented as an int. Returns None
        otherwise.
    :return:
        The locker number with sufficient digits unless len(lockerNum)
        > target number of digits, then returns None
    :rtype: str or None
    """
    try:
        int(lockerNum)
    except ValueError:
        return None

    digits = len(str(len(theDictionary)))

    if 1 <= len(lockerNum) <= digits:
        lockerNum = "0" * (digits - len(lockerNum)) + lockerNum
        return lockerNum


# discretionary
def textFileToDict (fileName, delimiter="\t"):
    """Reads fileName and converts its data into a dictionary.

    Correct line data format: "KEY[delimiter]VALUE\n"

    :param str fileName:
        The text file to pull data from
    :param str delimiter:
        The character separating key data from value data
    :return:
        A dictionary containing data du jour if data formatting is
        correct, else None
    :rtype: dict or None
    """
    dictionary = {}

    with open(fileName) as f:
        for line in f:
            # strips "\n"
            line = line.strip()
            keyAndValue = line.split(delimiter)
            # [0] strips "\n"
            if len(keyAndValue) == 2:
                dictionary[keyAndValue[0]] = keyAndValue[1]
            else:
                return None

    return dictionary


def totalStudents (theDictionary):
    """Identifies the total number of students assigned a locker.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :return:
        The total number of students assigned to a locker
    :rtype: int
    """
    total = 0

    for key in theDictionary:
        if (
            theDictionary[key] != "open" and
            theDictionary[key].isalpha()
        ):
            total += 1

    return total


def matchingByName (theDictionary, firstLetter):
    """Identifies students a name starting with firstLetter.

    Assumes student names are capitalized.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :param str firstLetter:
        The target letter by which to identify students. Currently does
        not check for only a single letter.
    :return:
        The students with name starting with firstLetter
    :rtype: list[str]
    """
    studentsByName = []
    firstLetter = firstLetter.upper()

    for key in theDictionary:
        if theDictionary[key][0] == firstLetter:
            studentsByName.append(theDictionary[key])

    return studentsByName


def matchingByLocker (theDictionary, lowerLimit, upperLimit):
    """Identifies students with lockers within a locker number range.

    Assumes locker numbers within theDictionary are sequential with no
    gaps in numbers.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :param int lowerLimit:
        The minimum number in range to identify students
    :param int upperLimit:
        The maximum number in range to identify students
    :return:
        The students with lockers within locker number limits if limits
        are possible given
    :rtype: list[str] or None
    """
    # if lower limit, upper limit not in range of len (theDictionary)
    lockerRange = range(int(firstLocker(theDictionary)),
                        int(lastLocker(theDictionary)) + 1)

    if (
        lowerLimit not in lockerRange or
        upperLimit not in lockerRange
    ):
        return None

    allLockers = list(theDictionary.keys())
    targetLockers = []
    for locker in range(lowerLimit - 1, upperLimit):
        targetLockers.append(allLockers[locker])

    studentList = []
    for key in targetLockers:
        if theDictionary[key] != "open":
            studentList.append(theDictionary[key])
    # doesn't need to be sorted, but why not?
    studentList.sort()

    return studentList


def firstLocker (theDictionary):
    """Identifies the first locker number.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :return:
        The first locker number in theDictionary
    :rtype: str
    """
    lockerCount = 1
    lockers = list(theDictionary.keys())

    for i in range(lockerCount):
        return lockers[i]


def lastLocker (theDictionary):
    """Identifies the last locker number.

    Assumes locker numbers within theDictionary are sequential with no
    gaps in numbers.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :return:
        The last locker number in theDictionary
    :rtype: str
    """
    lockerCount = len(theDictionary)
    lockers = list(theDictionary.keys())

    for i in range(lockerCount - 1, lockerCount):
        return lockers[i]


def findLocker (theDictionary, studentName):
    """Finds the locker(s) assigned to studentName.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :param str studentName:
        The name of the student(s) to find within theDictionary
    :return:
        The locker number(s) assigned to persons of name studentName
    :rtype: list[str] or None
    """
    lockers = []
    studentName = studentName.title()

    for key in theDictionary:
        if theDictionary[key] == studentName:
            lockers.append(key)

    if len(lockers) == 0:
        return None
    else:
        return lockers


def findStudent (theDictionary, lockerNum):
    """Identifies what student is assigned to lockerNum, if any.

    .. note::
        Current version has no error checking.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :param lockerNum:
        The locker to check for assignment
    :type lockerNum: str or int
    :return:
        The name of the student assigned to lockerNum or None if no
        assignment or if lockerNum is not in theDictionary
    :rtype: str or None
    """
    lockerNum = lockerNumDigits(str(lockerNum), theDictionary)

    if theDictionary[lockerNum] != "open":
        return theDictionary[lockerNum]


def students (theDictionary):
    """Identifies students with a locker and sorts them into a list.

    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :return:
        Sorted list of students with a locker
    :rtype: list[str]
    """
    studentList = []

    for key in theDictionary:
        if theDictionary[key] != "open":
            studentList.append(theDictionary[key])

    studentList.sort()

    return studentList


def printInfoSortedByStudent (title, theDictionary):
    """Prints locker assignment data sorted by student.

    Only accounts for lockers assigned to a student.

    :param str title:
        The title of the table to be printed out
    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :rtype: None
    """
    studentList = []
    studentColumn = 7
    lockerColumn = 6

    columnAdjustment = False
    for key in theDictionary:
        if theDictionary[key] != "open":
            studentList.append(theDictionary[key])
            columnAdjustment = True
        if columnAdjustment:
            if len(key) > lockerColumn:
                lockerColumn = len(key)
            if len(theDictionary[key]) > studentColumn:
                studentColumn = len(theDictionary[key])
        columnAdjustment = False

    studentList.sort()
    printStudent, printLocker = "Student", "Locker"

    print(title, end="\n\n")
    print(f"{printStudent:<{studentColumn}} | "
          f"{printLocker:<{lockerColumn}}")
    print("=" * (3 + studentColumn + lockerColumn))

    capturedKeys = []
    for student in studentList:
        for key in theDictionary:
            if (
                theDictionary[key] == student and
                key not in capturedKeys
            ):
                print(f"{student:<{studentColumn}} | "
                      f"{key:>{lockerColumn}}")
                capturedKeys.append(key)


def printInfoSortedByLocker (title, theDictionary):
    """Prints locker assignment data sorted by locker.

    Only accounts for lockers assigned to a student.

    :param str title:
        The title of the table to be printed out
    :param dict[str, str] theDictionary:
        key: locker number / value: student name or "open"
    :rtype: None
    """
    lockerList = []
    studentColumn = 7
    lockerColumn = 6

    columnAdjustment = False
    for key in theDictionary:
        if theDictionary[key] != "open":
            lockerList.append(key)
            columnAdjustment = True
        if columnAdjustment:
            if len(key) > lockerColumn:
                lockerColumn = len(key)
            if len(theDictionary[key]) > studentColumn:
                studentColumn = len(theDictionary[key])
        columnAdjustment = False

    lockerList.sort()
    printStudent, printLocker = "Student", "Locker"

    print(title, end="\n\n")
    print(f"{printLocker:<{lockerColumn}} | "
          f"{printStudent:<{studentColumn}}")
    print("=" * (3 + studentColumn + lockerColumn))

    capturedKeys = []
    for locker in lockerList:
        for key in theDictionary:
            if (
                key == locker and
                key not in capturedKeys
            ):
                print(f"{locker:>{lockerColumn}} | "
                      f"{theDictionary[key]:<{studentColumn}}")
                capturedKeys.append(key)


def main ():
    print("NOTICE:\nThis program was designed with lockers numbers as strings "
          "to represent a 3-digit locker number (e.g., \"001\").\n"
          "This program was designed that if lockers numbers (keys) are "
          "assigned \"open\" as values if a student is not assigned to "
          "that locker number.\n"
          "Program is submitted with \"locker_assignments.txt\" if the "
          "evaluator so chooses to use it.\n")
    print("Enter name of text file containing locker assignment data.")
    dataFile = promptTextFileRead()

    if not dataFile:
        print("Data file not found.\nExiting program.")
        exit()

    lockers = textFileToDict(dataFile)

    if not lockers:
        print("Locker assignment information not formatted correctly.\n"
              "Exiting program.")
        exit()

    # testing totalStudents
    print(f"Total number of students with a locker: {totalStudents(lockers)}")
    print()

    # testing matchingByName
    # no error checking currently
    letters = ["A", "D", "P"]
    for letter in letters:
        studentsByName = matchingByName(lockers, letter)
        if len(studentsByName) == 0:
            print(f"There are no students with names starting with "
                  f"\"{letter.upper()}\".")
        else:
            print(f"Student(s) with names starting with "
                  f"\"{letter.upper()}\": ", end="")
            last = len(studentsByName) - 1
            for i in range(len(studentsByName)):
                if i < last:
                    print(studentsByName[i], end=", ")
                else:
                    print(studentsByName[i])
    print()

    # testing matchingByLocker
    rangesToTest = [(1, 999), (1, 20), (100, 400), (0, 1000)]
    for t in range(len(rangesToTest)):
        minimum, maximum = rangesToTest[t]
        studentsByLocker = matchingByLocker(lockers, minimum, maximum)
        if studentsByLocker is None:
            print(f"Lower and upper limits must be between "
                  f"{firstLocker(lockers)} and {lastLocker(lockers)} "
                  f"respectively.")
        elif len(studentsByLocker) < 1:
            print(f"There a no students with lockers in range "
                  f"{lockerNumDigits(str(minimum), lockers)} to "
                  f"{lockerNumDigits(str(maximum), lockers)}.")
        else:
            print(f"Students with lockers in range "
                  f"{lockerNumDigits(str(minimum), lockers)} to "
                  f"{lockerNumDigits(str(maximum), lockers)}:\n\t"
                  f"{studentsByLocker}")
    print()

    # testing firstLocker
    print(f"The first locker number: {firstLocker(lockers)}")
    print()

    # testing lastLocker
    print(f"The last locker number: {lastLocker(lockers)}")
    print()

    # testing findLocker
    namesToTest = ["Jeff", "Benjamin", "Maxwell"]
    for name in namesToTest:
        locker = findLocker(lockers, name)
        if not locker:
            print(f"{name.title()} is not assigned a locker.")
        else:
            print(f"Locker(s) assigned to people of name "
                  f"\"{name.title()}\": ", end="")
            last = len(locker) - 1
            for i in range(len(locker)):
                if i < last:
                    print(locker[i], end=", ")
                else:
                    print(locker[i])
    print()

    # testing findStudent
    lockerNums = ["002", "004", "005"]
    for num in lockerNums:
        student = findStudent(lockers, num)
        if not student:
            print(f"There is no student assigned to locker number "
                  f"{num}.")
        else:
            print(f"Locker number {num} is assigned to {student}.")
    print()

    # testing students
    print(f"List of students with a locker:\n\t{students(lockers)}")
    print()

    # testing printInfoSortedByStudent
    title = "Locker Assignment Data Sorted by Student"
    printInfoSortedByStudent(title, lockers)
    print()

    # testing printInfoSortedByLocker
    title = "Locker Assignment Data Sorted by Locker"
    printInfoSortedByLocker(title, lockers)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

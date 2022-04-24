"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 11, Part 1
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    1. Prompt the user for a series of:
        - Student names
        - Locker numbers (keys) for the respective student
    2. Fill a dictionary with this data.
    3. Write the data to a text file.
        - Prompt the user for a file name to write the data to.
        - Each line is a key/value pair.
        - Insert a tab character between the key and the value.

Implementation:
    - Locker numbers with 3 digits (thus, a str) are used as keys.
    - Lockers with assignments have that student's name as the value
    - If a locker has no student assigned, it's value is "open".

Functions:
    createLockers (num)
        - Creates a dict for locker info.
    lockerNumDigits (lockerNum, digits)
        - Adds leading zeroes to ensure len (lockerNum) == digits.
    assignLocker (lockers):
        - Assigns students to a locker number within locker
    promptTextFileWrite ():
        - Prompts for desired text file name for use in write mode.
"""

from os.path import isfile


def createLockers (num=999):
    """Creates a dict for locker info.

    Locker keys are numerical strings with the same number of digits as
    num. Leading zeros are added as necessary. Each locker key is
    assigned a value of "open".

    :param int num:
    :return:
        The locker info dict
    :rtype: dict[str, str]
    """
    lockers = {}
    digits = len(str(num))

    for i in range(1, num + 1):
        zeroes = digits - len(str(i))
        locker = "0" * zeroes + str(i)
        lockers[locker] = "open"

    return lockers


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


def assignLocker (lockers):
    """Assigns students to a locker number within locker

    :param dict[str, str] lockers:
        A dict with locker numbers for keys and student names for
        values, unless locker is available in which case the value is
        "open"
    :return:
        lockers updated with student assignments
    :rtype: dict[str, str]
    """
    print ("Assign a student to a locker number.\n"
           "To finish assignment, press \"Enter\" for a student's name.")
    while True:
        name = input("Student's name: ").title ()
        if name == "":
            break
        else:
            singleName = name.split ()
            if len (singleName) != 1:
                # only done for assignment
                # ideally, a full student name would be accepted
                print("Enter only the student's first name.")
            else:
                while True:
                    digits = len (str (len (lockers)))
                    lockerPrompt = input (f"Locker number to assign to "
                                          f"{name}: ")
                    locker = lockerNumDigits (lockerPrompt, digits)
                    if (
                        not locker or
                        locker not in lockers
                    ):
                        min = lockerNumDigits ("1", digits)
                        max = str (len (lockers))
                        print (f"Locker number must be between "
                               f"{min} and {max}.")

                    elif lockers[locker] != "open":
                        print (f"Locker number {locker} is already assigned "
                               f"to {lockers[locker]}.")
                        overwrite_confirm = False

                        while True:
                            overwrite = input ("Overwrite locker assignment? "
                                               "(y/n): ").lower ()
                            if overwrite not in ["y", "yes", "n", "no"]:
                                print (f"{overwrite} is not a valid response.")
                            elif overwrite in ["y", "yes"]:
                                lockers[locker] = name
                                overwrite_confirm = True
                                break
                            else:
                                break

                        if overwrite_confirm:
                            break

                    else:
                        lockers[locker] = name
                        break


def promptTextFileWrite ():
    """Prompts for desired text file name for use in write mode.

    Designed to use in conjunction with writing of files, thus, checks
    if text file of same name already exists to circumvent undesired
    overwriting.

    :return:
        Name of text file to be (over)written
    :rtype: str
    """
    while True:
        fileName = input ("File name: ").lower ()
        if fileName[-4:] != ".txt":
            print ("File name must include \".txt\" extension.")
        elif not isfile(fileName):
            return fileName
        else:
            print(fileName, "already exists. Do wish to overwrite?")
            while True:
                overwritePrompt = input("y/n: ").lower()
                if overwritePrompt in ["y", "yes"]:
                    return fileName
                elif overwritePrompt in ["n", "no"]:
                    break


def main():
    lockers = createLockers ()

    assignLocker (lockers)

    print ("Name the file to store your locker assignment data to.")
    fileName = promptTextFileWrite ()

    with open (fileName, "w") as f:
        for line in lockers:
            f.write (f"{line}\t{lockers[line]}\n")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

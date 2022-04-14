"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 10, Part 1
Copyright (C) 2022 Kenneth Jahnke

Prompt the user for a series of class names and the number of credits
for each class. The class name must be in "DEPT NUM" format, for
example, "CSCI 160". Assign every valid entry to a dictionary with the
class as a string and the number of credits as an integer. Continue to
ask for classes until the user enters a blank value.

Prompt the user for a file name. Write the key-value pairs to the file
with one pair per line and a tab character ("\t") between the key and
value.

Functions:

    classStringValidator (className)
        - Checks if className is a valid class name.
    # TODO
"""

from os.path import isfile


def classStringValidator (className):
    """Checks if className is a valid class name.

    Format of string: DEPT NUM
    Allows for department names of 2-4 characters. Examples:
        - EE 101
        - FIN 310
        - CSCI 160
    Allows for lab and honors classes. Examples
        - BIOL 150L
        - CSCI 493HON

    :param str className: The name of the class to be validated
    :except AttributeError: className must be string
    :return: The name of class if valid, else None
    :rtype: str or None
    """
    try:
        className = className.upper()
    except AttributeError:
        return None
    # min example: "EE 101"  --> len == 6
    # max example: "CSCI 493HON" --> len == 11
    if len (className) in range (6, 12):
        departmentClassNumberSplit = className.split ()
        if len (departmentClassNumberSplit) == 2:
            department = departmentClassNumberSplit[0]
            classNumber = departmentClassNumberSplit[1]
            #
            if (
                # department could be 2 to 4 chars
                # examples: EE, FIN, CSCI
                len (department) in range (2, 5) and
                department.isalpha () and
                len (classNumber) in range (3, 7) and
                classNumber[:3].isnumeric ()
            ):
                # account for honor and lab courses
                if (
                    len (classNumber) == 3 or
                    classNumber[3:] == "HON" or
                    classNumber[3:] == "L"
                ):
                    return className


# TODO
def creditsValidator ():
    """check that the value for credits can be converted
    to an in and that the value is between 1 and 4 inclusive"""
    """fdsaf
    
    :param:
    
    """
    # TODO
    try:
        pass
    # TODO for function that uses "if variable is not None"
    except ValueError:
        return None


# TODO modify
def promptTempsDataFileName ():
    # TODO modify
    """Prompts user for name of data file containing temperature data.

    Must include file extension, e.g., .txt.
    Data format contract:
        - Line 1: "Month Year", e.g., "March 2022"
        - Line 2 - Line n. 'Day,HighTemp,LowTemp', e.g., "10,69,30"

    .. warning::
        Excessive blank lines within (> 0) or at end of data (> 1) may
        cause exceptions if data file is argument of certain functions.

    :return: The temperature data file name if file exists
    :rtype: str or None
    """
    while True:
        fileName = input(
            "Enter name of temperature data file (include extension): ")
        if isfile(fileName):
            return fileName
        elif fileName == "":
            break
        else:
            print(f"{fileName} does not exist.\n"
                  "Try entry again or press 'Enter'.")


# TODO modify
def promptFileNameWrite ():
    # TODO modify
    """Prompts user for desired name of text file for use in writing modes.

    Designed to use in conjunction with writing of files, thus, checks if
    text file of same name already exists to circumvent undesired
    overwriting.

    :return: The name of a .txt file
    :rtype: str
    """
    while True:
        fileName = input("Enter desired text file name. Do not add a file "
                         "extension.\nFile name: ")
        fileName = fileName + ".txt"
        if not isfile(fileName):
            return fileName
        else:
            print(fileName, "already exists. Do wish to overwrite?")
            while True:
                overwritePrompt = input("y/n: ").lower()
                if overwritePrompt in ["y", "yes"]:
                    return fileName
                elif overwritePrompt in ["n", "no"]:
                    break




# TODO modify
def promptFileNameRead ():
    # TODO modify
    """Prompts user for desired name of text file for use in read mode.

    Designed to use in conjunction with writing of files, thus, checks if
    text file of same name already exists to circumvent undesired
    overwriting.

    :return: The name of a .txt file
    :rtype: str
    """
    while True:
        fileName = input("Enter desired text file name. Do not add a file "
                         "extension.\nFile name: ")
        fileName = fileName + ".txt"
        if isfile(fileName):
            return fileName
        # FIXME for reading
        else:
            print(fileName, "already exists. Do wish to overwrite?")
            while True:
                overwritePrompt = input("y/n: ").lower()
                if overwritePrompt in ["y", "yes"]:
                    return fileName
                elif overwritePrompt in ["n", "no"]:
                    break





# if numCredits not in range (0, 5):
    # prompt "are you sure?"

def main():
    print(promptFileName())


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

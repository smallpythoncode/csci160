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

    classNameValidator (className)
        - Checks if className is a valid class name.
    creditsValidator (creditsValue)
        - Check that creditsValue is valid number of credits.
    promptFileNameWrite ()
        - Prompts for desired text file name for use in write mode.
    promptFileNameRead ()
        - Prompts for desired text file name for use in read mode.

"""

from os.path import isfile


def classNameValidator (className):
    """Checks if className is a valid class name.

    Format of string: DEPT NUM
    Allows for department names of 2-4 characters. Examples:
        - EE 101
        - FIN 310
        - CSCI 160
    Allows for lab and honors classes. Examples:
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


def creditsValidator (creditsValue):
    """Check that creditsValue is valid number of credits.

    Credit range: 1 <= creditsValue <= 4
    
    :param int creditsValue: The number of credits to check
    :except TypeError: creditsValue should be an int
    :return: The number of credits if valid, else None
    :rtype: int or None
    
    """
    try:
        if 1 <= creditsValue <= 4:
            return creditsValue
    except TypeError:
        return None


def promptFileNameWrite ():
    """Prompts for desired text file name for use in write mode.

    Designed to use in conjunction with writing of files, thus, checks
    if text file of same name already exists to circumvent undesired
    overwriting. Returns name of text file to be (over)written or None
    if overwrite denied.

    :return: The name of a .txt file
    :rtype: str or None
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


def promptFileNameRead ():
    """Prompts for desired text file name for use in read mode.

    Designed to use in conjunction with reading of files. Returns name
    of text file if it exists, otherwise None.

    .. note::
        Does not contribute to Program 10-1 assignment; written for
        personal use.

    :return: The name of a .txt file
    :rtype: str
    """
    while True:
        fileName = input("Enter desired text file name. Do not add a file "
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


def main ():
    classesAndCredits = {}
    print ("Enter a series of class names and credits for each class.\n"
           "Class names must be in \"DEPT NUM(L/HON)\" format. Examples:\n\t"
           "CSCI 160, EE 101, BIOL 150L\n"
           "The number of credits must be an integer between 1 and 4"
           "(inclusive)\n"
           "To exit, press \"ENTER\" during class name prompt.\n")

    while True:
        className = input("Class name: ").strip ()
        if className == "":
            break
        else:
            className = classNameValidator (className)
            if className is None:
                print ("That is not a valid class name.")
            elif className in classesAndCredits:
                while True:
                    overwrite = input (f"Data already entered for {className}."
                                       f" Overwrite? (y/n): ").lower ()
                    if overwrite in ["y", "yes"]:
                        while True:
                            numCredits = int (
                                input(f"{className} credits: ").strip ()
                            )
                            numCredits = creditsValidator (numCredits)
                            if numCredits is None:
                                print (f"{numCredits} is not a valid number "
                                       f"of credits")
                            else:
                                classesAndCredits[className] = numCredits
                                print ()
                                break
                        break
                    elif overwrite in ["n", "no"]:
                        break
                    else:
                        print (f"{overwrite} is not a valid response.")
            else:
                while True:
                    numCredits = int (
                                input(f"{className} credits: ").strip ()
                    )
                    numCredits = creditsValidator (numCredits)
                    if numCredits is None:
                        print (f"{numCredits} is not a valid number of "
                              f"credits")
                    else:
                        classesAndCredits[className] = numCredits
                        print()
                        break

    print ()
    print ("The data will be written to a text file.")
    while True:
        fileName = promptFileNameWrite ()
        if fileName is not None:
            break

    with open(fileName, "w") as f:
        for i in classesAndCredits:
            f.write (f"{i}\t{classesAndCredits[i]}\n")

    print (f"Data writing complete. Check working directory for {fileName}")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

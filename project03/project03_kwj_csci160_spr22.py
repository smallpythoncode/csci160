"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Project 03
Copyright (C) 2022 Kenneth Jahnke

# FIXME due Monday, May 9

# TODO
Assignment:



# TODO
Required Functions:
    readClassInfo(fileName)
        - #TODO
    writeClassInfo(fileName, classes)
        - #TODO
    addClass(classes, className, grade, credits)
        - Adds className, grade, and credits to classes.
    attemptedCredits(classes)
        - #TODO
    passedCredits(classes)
        - #TODO
    printClasses(classes)
        - #TODO
    getGPA(classes)
        - #TODO
    updateGrade(classes, className, newGrade)
        - #TODO
    classStatus(classes)
        - #TODO
    main()
        - Testing all of the required functions.
        # TODO
        Order of testing:
            1. fdsa
            #. fdsa
            #. fdsa
            #. fdsa
            #. fdsa
            #. fdsa
            #. fdsa
            #. fdsa
            #. fdsa
            #. fdsa
            #. fdsa

# TODO
Discretionary Functions:
    standardHonorPoints()
        - Establishes the standard system of honor points by grade.




"""


# discretionary
def standardHonorPoints():
    """Establishes the standard system of honor points by grade.

    :return:
        A dictionary with grades as the keys and standard number of
        honor points as the respective value.
    :rtype: dict[str, int]
    """
    honorPoints = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "F": 0
    }

    return honorPoints


# TODO
def readClassInfo(fileName):
    """

    :param str fileName:
        The name of the text file containing class information.
    :return:
        The class information. Format:
            classes = {className: {"grade": grade, "credits", credits}}
    :rtype: dict
    """
    classInfo = {}

    with open(fileName, "r") as f:
        for line in f:
            tempClassInfo = line
            className, grade, numCredits = tempClassInfo.split("\t")

            addClass(classInfo, className, grade, numCredits)

    return classInfo


# TODO
def writeClassInfo(fileName, classes):
    pass


def addClass(classes, className, grade, credits):
    """Adds className, grade, and credits to classes.

    Only adds information to classes if className is not already in
    classes.

    .. note::
        credits parameter shadows built-in function credits(). If not
        mandated by assignment instructions, parameter name would be
        altered to numCredits.

    :param dict classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits", credits}}
    :param str className:
        The name of the class to be added to classes.
    :param str grade:
        The grade received for className.
    :param int credits:
        The number of credits className is worth.
    :return:
        Returns True if className added to classes (i.e., className was
        not already in classes), else False.
    :rtype: bool
    """
    if className in classes:
        return False
    else:
        className = className.upper()
        grade = grade.upper()
        credits = int(credits)
        classes[className] = {"grade": grade, "credits": credits}
        return True


# TODO
def attemptedCredits(classes):
    pass


# TODO
def passedCredits(classes):
    pass


# TODO
def printClasses(classes):
    pass


# TODO
def getGPA(classes):
    pass


# TODO
def updateGrade(classes, className, newGrade):
    pass


# TODO
def classStatus(classes):
    pass


# TODO
def main():
    """Testing all of the required functions.

    :rtype: None
    """
    honorPoints = standardHonorPoints()
    print(honorPoints)

    print("\nTesting readClassInfo:")
    # TODO

    print("\nTesting addClass:")
    # TODO

    print("\nTesting updateGrade:")
    # TODO

    print("\nTesting writeClassInfo:")
    # TODO

    print("\nTesting attemptedCredits:")
    # TODO

    print("\nTesting passedCredits:")
    # TODO

    print("\nTesting printClasses:")
    # TODO

    print("\nTesting getGPA:")
    # TODO

    print("\nTesting classStatus:")
    # TODO







    classes = {}
    print(classes)
    if addClass(classes, "math 107", "a", 4):
        print("yolo")
    print(classes)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

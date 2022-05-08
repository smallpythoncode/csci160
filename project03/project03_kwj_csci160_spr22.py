"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Project 03
Copyright (C) 2022 Kenneth Jahnke

# FIXME due Monday, May 9

Assignment:
    - Write a text file with each line containing class name, grade for
    class, and the number of credits the class is worth. Separate data
    elements by a tab character.
    - Write the required functions to display/manipulate the data and
    test each in function main.

# TODO
Required Functions:
    readClassInfo(fileName)
        - Read class data from fileName.
    writeClassInfo(fileName, classes)
        - Writes class data in classes to fileName.
    addClass(classes, className, grade, credits)
        - Adds className, grade, and credits to classes.
    attemptedCredits(classes)
        - #TODO
    passedCredits(classes)
        - #TODO
    printClasses(classes)
        - Print class info an orderly table followed by the GPA.
    getGPA(classes)
        - Calculates the GPA based on data in classes.
    updateGrade(classes, className, newGrade)
        - Updates grade for className to newGrade.
    classStatus(classes)
        - #TODO
    main()
        - Testing all of the required functions.
        Order of testing:
            1. readClassInfo
            #. addClass
            #. updateGrade
            #. writeClassInfo
            #. printClasses
            #. attemptedCredits
            #. passedCredits
            #. getGPA
            #. classStatus

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


def readClassInfo(fileName):
    """Read class data from fileName.

    Format: Each line contains className, grade, and numCredits. Each
    element of line is separated by a tab character.

    :param str fileName:
        The name of the text file containing class information.
    :return:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :rtype: dict
    """
    classInfo = {}

    with open(fileName, "r") as f:
        for line in f:
            tempClassInfo = line
            className, grade, numCredits = tempClassInfo.split("\t")

            addClass(classInfo, className, grade, numCredits)

    return classInfo


def writeClassInfo(fileName, classes):
    """Writes class data in classes to fileName.

    Format: Each line contains className, grade, and numCredits. Each
    element of line is separated by a tab character.

    :param str fileName:
        The name of the text file to write classes data to.
    :param dict classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :rtype: None
    """
    with open(fileName, "w") as f:
        classNames = list(classes.keys())
        for n in classNames:
            gradeCredits = list(classes[n].values())

            line = f"{n:s}\t{gradeCredits[0]:s}\t{gradeCredits[1]:d}\n"
            f.write(line)


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
    """Print class info an orderly table followed by the GPA.

    :param classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :rtype: None
    """
    pass


def getGPA(classes):
    """Calculates the GPA based on data in classes.

    :param classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :return:
        The GPA.
    :rtype: float
    """
    honorPointSystem = standardHonorPoints()
    numCredits = 0
    honorPoints = 0
    classList = list(classes.keys())

    for c in classList:
        numCredits += classes[c]["credits"]

        grade = classes[c]["grade"]
        honorPoints += honorPointSystem[grade] * classes[c]["credits"]

    gpa = honorPoints / numCredits

    return gpa


def updateGrade(classes, className, newGrade):
    """Updates grade for className to newGrade.

    :param dict classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :param str className:
        The class for which the grade is to be updated.
    :param str newGrade:
        The updated grade.
    :return:
        Returns True if className was assigned newGrade (i.e.,
        className is in classes), else False.
    :rtype: bool
    """
    if className not in classes:
        return False
    else:
        className = className.upper()
        newGrade = newGrade.upper()
        # numCredits = classes["credits"]

        classes[className]["grade"] = newGrade

        return True


# TODO
def classStatus(classes):
    pass


# TODO
def main():
    """Testing all of the required functions.

    :rtype: None
    """

    print("\nTesting readClassInfo:")
    initialDataFile = "initial_class_info.txt"
    classes = readClassInfo(initialDataFile)
    print(f"Class info from {initialDataFile}:\n\t{classes}")

    print("\nTesting addClass:")
    classesInfoToAdd = [
        # different cases/types to display data is
        # formatted at processing
        ["MATH 107", "B", 3],
        ["math 208", "a", "3"]
    ]

    for newClass in classesInfoToAdd:
        className, grade, numCredits = newClass[0], newClass[1], newClass[2]
        className = className.upper()

        addedClass = addClass(classes, className, grade, numCredits)

        if addedClass:
            print("{} was added to class info with a grade of {} and credit "
                  "value of {}.".format(
                    className,
                    classes[className]["grade"],
                    classes[className]["credits"]
                    )
                  )
        else:
            print(f"{className} is already in the class information.")

    print("\nTesting updateGrade:")
    gradesToUpdate = [
        # different cases/types to display data is
        # formatted at processing
        ["ACCT 200", "C"],
        ["math 107", "a"]
    ]

    for grade in gradesToUpdate:
        className, newGrade = grade[0], grade[1]
        className = className.upper()

        updatedGrade = updateGrade(classes, className, newGrade)

        if updatedGrade:
            print("The grade for {} was updated to {}.".format(
                    className,
                    classes[className]["grade"]
                    )
                  )
        else:
            print(f"{className} is not in the class information.")

    print("\nTesting writeClassInfo:")
    updatedDataFile = "updated_class_info.txt"
    print(f"Class info to print to {updatedDataFile}:\n\t{classes}")
    writeClassInfo(updatedDataFile, classes)

    print("\nTesting printClasses:")
    # TODO

    print("\nFor demonstration of functionality, we will look at "
          "Student 1 and Student 2.")
    student1 = classes
    student2 = readClassInfo("student2_class_info")
    print(f"Class info for Student 1:\n\t{student1}")
    print(f"Class info for Student 2:\n\t{student2}")

    print("\nTesting attemptedCredits:")
    # TODO

    print("\nTesting passedCredits:")
    # TODO

    print("\nTesting getGPA:")
    print(f"Student 1 GPA: {getGPA(student1):.3f}")
    print(f"Student 2 GPA: {getGPA(student2):.3f}")

    print("\nTesting classStatus:")
    # TODO


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

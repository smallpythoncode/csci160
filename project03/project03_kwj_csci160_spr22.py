"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Project 03
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    - Write a text file with each line containing class name, grade for
      class, and the number of credits the class is worth. Separate data
      elements by a tab character.
    - Write the required functions to display/manipulate the data and
      test each function main.

Required Functions:
    readClassInfo(fileName)
        - Read class data from fileName.
    writeClassInfo(fileName, classes)
        - Writes class data in classes to fileName.
    addClass(classes, className, grade, credits)
        - Adds className, grade, and credits to classes.
    attemptedCredits(classes)
        - Calculates the number of credits a student attempted.
    passedCredits(classes)
        - Calculates the number of credits a student passed.
    printClasses(classes)
        - Print class info an orderly table followed by the GPA.
    getGPA(classes)
        - Calculates the GPA based on data in classes.
    updateGrade(classes, className, newGrade)
        - Updates grade for className to newGrade.
    classStatus(classes)
        - Determines the class status of the student based on credits.
    main()
        - Testing all of the required functions.
        Order of testing:
            1. readClassInfo
            2. addClass
            3. updateGrade
            4. writeClassInfo
            5. printClasses
            6. attemptedCredits
            7. passedCredits
            8. getGPA
            9. classStatus

Discretionary Functions:
    standardHonorPoints()
        - Establishes the standard system of honor points by grade.

Accompanying Text Files:
    initial_class_info.txt
        - The file mandated by assignment (See Assignment section).
    updated_class_info.txt
        - A copy of the file that results from main testing of
          writeClassInfo
    student2_class_info.txt
        - An alternate data file that could be used via readClassInfo

.. note::
    Original lines 385, 386 left in for insight into development
    process. Dev elected to comment these out and hard code Student 1
    data at lines 388-392 and Student 2 data at lines 393-416 to ensure
    functionality at assignment turn-in.
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


def attemptedCredits(classes):
    """Calculates the number of credits a student attempted.

    :param dict classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :return:
        The number of credits the student attempted.
    :rtype: int
    """
    numCredits = 0
    classList = list(classes.keys())

    for c in classList:
        numCredits += classes[c]["credits"]

    return numCredits


def passedCredits(classes):
    """Calculates the number of credits a student passed.

    :param dict classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :return:
        The number of credits the student passed.
    :rtype: int
    """
    numCredits = 0
    classList = list(classes.keys())

    for c in classList:
        if classes[c]["grade"] != "F":
            numCredits += classes[c]["credits"]

    return numCredits


def printClasses(classes):
    """Print class info an orderly table followed by the GPA.

    :param dict classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :rtype: None
    """
    classNum = 1
    classList = list(classes.keys())

    print("{} {:<11}   {}   {}".format(" " * 3, "Class", "Grade", "Credits"))
    for c in classList:
        counter = str(classNum) + "."
        print("{:<3s} {:<11s}   {:^5s}   {:>7d}".format(
                counter,
                c,
                classes[c]["grade"],
                classes[c]["credits"]
                )
              )
        classNum += 1

    print(f"\nOverall GPA: {getGPA(classes)}")


def getGPA(classes):
    """Calculates the GPA based on data in classes.

    :param dict classes:
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


def classStatus(classes):
    """Determines the class status of the student based on credits.

    :param dict classes:
        The class information. Format:
            classes = {className: {"grade": grade, "credits",
            numCredits}}
    :return:
        The status of the student.
    :rtype: str
    """
    uniYears = {"Freshman": 0, "Sophomore": 24, "Junior": 60, "Senior": 90}
    statuses = reversed(list(uniYears.keys()))
    numCreditsPassed = passedCredits(classes)

    for status in statuses:
        if numCreditsPassed >= uniYears[status]:
            return status


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
    printClasses(classes)

    print("\nFor demonstration of functionality, we will look at data for "
          "Student 1 and Student 2.")
    # student1 = classes
    # student2 = readClassInfo("student2_class_info.txt")
    # hard coded to ensure functionality at assignment turn-in
    student1 = {
        'CSCI 160': {'grade': 'A', 'credits': 4},
        'MATH 107': {'grade': 'A', 'credits': 4},
        'MATH 208': {'grade': 'A', 'credits': 3}
    }
    student2 = {
        'CSCI 160': {'grade': 'A', 'credits': 4},
        'MATH 107': {'grade': 'A', 'credits': 4},
        'MATH 208': {'grade': 'C', 'credits': 3},
        'CSCI 161': {'grade': 'C', 'credits': 4},
        'CSCI 289': {'grade': 'B', 'credits': 3},
        'MATH 165': {'grade': 'A', 'credits': 4},
        'CSCI 242': {'grade': 'A', 'credits': 3},
        'MATH 166': {'grade': 'A', 'credits': 4},
        'CSCI 265': {'grade': 'B', 'credits': 3},
        'EE 201': {'grade': 'A', 'credits': 3},
        'EE 201L': {'grade': 'A', 'credits': 1},
        'CSCI 266': {'grade': 'B', 'credits': 3},
        'BIOL 150': {'grade': 'C', 'credits': 3},
        'BIOL 150L': {'grade': 'C', 'credits': 1},
        'CSCI 330': {'grade': 'A', 'credits': 3},
        'BIOL 151': {'grade': 'F', 'credits': 3},
        'BIOL 151L': {'grade': 'F', 'credits': 1},
        'MATH 321': {'grade': 'C', 'credits': 3},
        'CSCI 280': {'grade': 'B', 'credits': 3},
        'CSCI 327': {'grade': 'A', 'credits': 3},
        'CSCI 384': {'grade': 'C', 'credits': 3},
        'CSCI 370': {'grade': 'A', 'credits': 4}
    }
    print(f"Class info for Student 1:\n\t{student1}")
    print(f"Class info for Student 2:\n\t{student2}")

    print("\nTesting attemptedCredits:")
    print(f"Student 1's attempted credits: {attemptedCredits(student1)}")
    print(f"Student 2's attempted credits: {attemptedCredits(student2)}")

    print("\nTesting passedCredits:")
    print(f"Student 1's passed credits: {passedCredits(student1)}")
    print(f"Student 2's passed credits: {passedCredits(student2)}")

    print("\nTesting getGPA:")
    print(f"Student 1 GPA: {getGPA(student1):.3f}")
    print(f"Student 2 GPA: {getGPA(student2):.3f}")

    print("\nTesting classStatus:")
    print(f"Class status of Student 1: {classStatus(student1)}")
    print(f"Class status of Student 2: {classStatus(student2)}")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

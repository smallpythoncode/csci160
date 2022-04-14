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

    # TODO
"""


def classStringValidator (className):
    """# TODO

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






# if numCredits not in range (0, 5):
    # prompt "are you sure?"

def main():
    pass


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

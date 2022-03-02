"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 06 Part A

Write the required functions with  proper documentation, i.e., a
docstring with a descriptions of what it does, its parameters, and its
return value.

Test all the functions in the main code.

Functions:

    def square (intValue):
        Squares an integer.
    def isOdd (intValue):
        Determines if an integer is odd.
    def isEven(intValue):
        Determines if an integer is even.
    def sumOfOdds (intValue):
        Determines sum of odds in range of 1 to specified integer.
    def sumOfSquares (intValue):
        Determines sum of squares in range of 1 to specified integer.
    def compareTo (intValue1, intValue2):
        Compares two integers.

Developer Note:

    From PEP 8:
        "Function names should be lowercase, with words separated by
        underscores as necessary to improve readability."
    Functions within this module are written in camelCase only because
    the assignment instructions specify as such:
        "The function header MUST be written as specified."
"""


# TODO
def square (intValue):
    """Squares an integer.

    Assignment:
    This function returns the square of intValue.

    :param intValue: Integer to be squared
    :type intValue: int
    :return: Square of intValue
    :rtype: int # TODO verify
    """
    pass


# TODO
def isOdd (intValue):
    """Determines if an integer is odd.

    Assignment:
    This function will return True if intValue is odd, otherwise it
    returns False.

    # TODO
    :param intValue:
    :return:
    """
    pass


# TODO
def isEven(intValue):
    """Determines if an integer is even.

    Assignment:
    This function will return True if intValue is even, otherwise it
    return False. This function MUST use isOdd to determine the returned
    value. The point behind this function is to minimize the amount of
    redundant work that is done in our code, not that determining odd or
    even is a lot of work. It’s the concept more than the reality of the
    code in this case.

    # TODO
    :param intValue:
    :return:
    """
    pass


# TODO
def sumOfOdds (intValue):
    """Determines sum of odds in range of 1 to specified integer.

    Assignment:
    This function returns the summation of 1 to intValue of the odd
    values in the range. You can assume that intValue will be positive.
    For example, sumOfOdds(5) would return 9 (1 + 3 + 5).

    # TODO
    :param intValue:
    :return:
    """
    pass


# TODO
def sumOfSquares (intValue):
    """Determines sum of squares in range of 1 to specified integer.

    Assignment:
    This function returns the sum of the squares from 1 to intValue. For
    example, sumOfSquares(5) would return 55 (1 + 4 + 9 + 16 + 25). You
    MUST use a loop and the square function to determine the returned
    value.

    # TODO
    :param intValue:
    :return:
    """
    pass


# TODO
def compareTo (intValue1, intValue2):
    """Compares two integers.

    Assignment:
    This functions returns -1 if intValue1 is less than intValue2,
    returns 1 if intValue1 is greater than intValue2, or returns 0 if
    intValue1 is equal to intValue2.

    # TODO
    :param intValue1:
    :param intValue2:
    :return:
    """
    pass


def main():
    pass


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

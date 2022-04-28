"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 12, Part 2
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    # TODO

.. note::
    Function HEADERS are written exactly as specified per assignment
    instructions, i.e., written in camelCase with whitespace between the
    function's name and its parameters. camelCase persists for
    declaration of variables for consistency. When a function is called,
    the absence of whitespace between a function's name and its
    arguments was judged to have no effect on performance; thus, such
    whitespace is excluded outside of function headers.

# TODO
Required Functions:
    fdsa



# TODO
Discretionary Functions:
    textFileToDict (fileName, delimiter="\t"):
        - Reads fileName and converts its data into a dict.




"""

from statistics import mean


# discretionary
def textFileToDict (fileName, kType="s", vType="s", delimiter="\t"):
    """Reads fileName and converts its data into a dict.

    Correct line data format: "KEY[delimiter]VALUE".

    :param str fileName:
        The text file to pull data from.
    :param str kType:
        The target data type of keys assigned to the dict: "s" for str;
        "i" for int; "f" for float.
    :param str vType:
        The target data type of values assigned to the dict: "s" for
        str; "i" for int; "f" for float.
    :param str delimiter:
        The character separating key data from value data.
    :return:
        A dictionary containing desired data.
    :rtype: dict or None
    :except ValueError:
        Will return None if data is formatted incorrectly or data is
        incapable of being converted to target kType/vType.
    """
    dictionary = {}
    validTypes = {"s": str, "i": int, "f": float}

    if (
        kType not in validTypes or
        vType not in validTypes
    ):
        return None

    kType = validTypes[kType]
    vType = validTypes[vType]

    with open(fileName) as f:
        for line in f:
            # strips "\n"
            line = line.strip()
            try:
                key, value = line.split(delimiter)
            except ValueError:
                return None

            try:
                if kType == int:
                    key = float(key)
                    key = kType(key)
                else:
                    key = kType(key)

                if vType == int:
                    value = float(value)
                    value = vType(value)
                else:
                    value = vType(value)
            except ValueError:
                return None

            dictionary[key] = value

    return dictionary


def readMenuItems (fileName):
    """Fills a dict with menu items and price data from fileName.

    :param str fileName:
        Text file containing lines of menu items followed by prices
        separated by a tab character.
    :return:
        Dict with menu items as keys and prices as values.
    :rtype: dict[str, float]
    """
    dictionary = textFileToDict(fileName, "s", "f")

    return dictionary



# TODO
def totalMenuItems (theDictionary):
    """
    # TODO

    :param dict[str, float] theDictionary:

    :return:

    :rtype:
    """
    pass


# TODO
def getMenuItems (theDictionary):
    """
    # TODO
    :param dict[str, float] theDictionary:

    :return:

    :rtype:
    """
    pass


# TODO
def getMenuItemsWithinRange (theDictionary, lowerLimit, upperLimit):
    """
    # TODO

    :param dict[str, float] theDictionary:

    :param float or int lowerLimit:

    :param float or int upperLimit:

    :return:

    :rtype:
    """
    pass


# TODO
def addMenuItem(theDictionary, item, price):
    """
    # TODO
    :param dict[str, float] theDictionary:

    :param str item:

    :param float or int price:

    :return:

    :rtype:
    """
    pass


# TODO
def updateMenuItem (theDictionary, item, price):
    """
    # TODO
    :param dict[str, float] theDictionary:

    :param str item:

    :param float or int price:

    :return:

    :rtype:
    """
    pass


# TODO
def getMenuItemPrice (theDictionary, item):
    """
    # TODO
    :param dict[str, float] theDictionary:

    :param str item:

    :return:

    :rtype: float
    """
    pass


# TODO
def averagePrice (theDictionary):
    """
    # TODO
    :param dict[str, float] theDictionary:

    :return:

    :rtype: float
    """
    pass


# TODO
def takeOrder (theDictionary):
    """
    # TODO
    :param dict[str, float] theDictionary:

    :return:

    :rtype:
    """
    pass


# TODO
def printMenu (theDictionary):
    """
    # TODO
    :param dict[str, float] theDictionary:

    :rtype: None
    """
    pass


def main():
    # FIXME
    fileName = "burger_menu.txt"
    x = readMenuItems(fileName)
    print(x)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

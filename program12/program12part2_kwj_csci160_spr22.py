"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 12, Part 2
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    1. Write the required functions.
    #. Prompt user for text file name containing menu data.
    #. Display/manipulate the data as prescribed by required functions.

.. note::
    Assignment instructions declare "avergePrice (theDictionary)". The
    decision was made to correct the spelling error and it this program
    write the function name as "averagePrice".

.. note::
    DATA FORMAT - Menu items (keys): uppercase strings; prices: floats
    (within dicts) or string depictions of floats (if in a file).
    Deviation of this format may produce undesirable results.

.. note::
    Function HEADERS are written exactly as specified per assignment
    instructions, i.e., written in camelCase with whitespace between the
    function's name and its parameters. camelCase persists for
    declaration of variables for consistency. When a function is called,
    the absence of whitespace between a function's name and its
    arguments was judged to have no effect on performance; thus, such
    whitespace is excluded outside of function headers.

Required Functions:
    readMenuItems (fileName)
        - Fills a dict with menu items and price data from fileName.
    totalMenuItems (theDictionary)
        - Calculates the total number of items available on menu
    getMenuItems (theDictionary):
        - Identify what items are on the menu.
    getMenuItemsWithinRange (theDictionary, lowerLimit, upperLimit):
        - Identifies menu items that are in specified price range.
    addMenuItem(theDictionary, item, price):
        - Adds an item to the menu.
    updateMenuItem (theDictionary, item, price):
        - Update the price of item.
    getMenuItemPrice (theDictionary, item)
        - Identifies the price of item.
    averagePrice (theDictionary)
        - Identifies the average price of items on the menu.
    takeOrder (theDictionary)
        - Create a mock order for a number of items from the menu.
    printMenu (theDictionary)
        - Prints a table of menu items and prices.

Discretionary Functions:
    promptTextFileRead ()
        - Prompts for desired text file name for use in read mode.
    textFileToDict (fileName, kType="s", vType="s", delimiter=":")
        - Reads fileName and converts its data into a dict.
"""

from os.path import isfile
from random import randint
from statistics import mean


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
def textFileToDict (fileName, kType="s", vType="s", delimiter=":"):
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

    This functions does no error checking as the assignment instructions
    outline. However, its parent function (textFiletoDict) will return
    to this function None if fileName is improperly formatted.

    :param str fileName:
        Text file containing lines of menu items followed by prices
        separated by a tab character.
    :return:
        Dict with menu items as keys and prices as values.
    :rtype: dict[str, float]
    """
    dictionary = textFileToDict(fileName, "s", "f", "\t")

    return dictionary


def totalMenuItems (theDictionary):
    """Calculates the total number of items available on menu
    (theDictionary).

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :return:
        Total number of items on the menu.
    :rtype: int
    """
    return len(theDictionary)


def getMenuItems (theDictionary):
    """Identify what items are on the menu.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :return:
        A sorted list of menu items.
    :rtype: list[str]
    """
    items = sorted(list(theDictionary.keys()))

    return items


def getMenuItemsWithinRange (theDictionary, lowerLimit, upperLimit):
    """Identifies menu items that are in specified price range.

    Rounds lowerLimit and upperLimit to a valid dollar/cent value.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :param float or int lowerLimit:
        The minimum price to check for menu items.
    :param float or int upperLimit:
        The maximum price to check for menu items.
    :return:
        The menu items whose prices are within the specified price
        range.
    :rtype:
    """
    items = getMenuItems(theDictionary)
    inRangeItems = []

    for item in items:
        if lowerLimit <= theDictionary[item] <= upperLimit:
            inRangeItems.append(item)

    return inRangeItems


def addMenuItem(theDictionary, item, price):
    """Adds an item to the menu.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :param str item:
        The name of the new item to be added to the menu.
    :param float or int price:
        The price of item.
    :return:
        True if item added to the menu or False if item was already on
        the menu.
    :rtype: bool
    """
    item = item.upper()
    price = round(float(price), 2)

    if item in theDictionary:
        return False

    theDictionary[item] = price

    return True


def updateMenuItem (theDictionary, item, price):
    """Update the price of item.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :param str item:
        The item whose price is to be updated.
    :param float or int price:
        The updated price of item.
    :return:
        True if item exists on the menu, else False.
    :rtype: bool
    """
    item = item.upper()
    price = round(float(price), 2)

    if item in theDictionary:
        theDictionary[item] = price
        return True

    return False

    # if item not in theDictionary:
    #     return False
    #
    # theDictionary[item] = price
    #
    # return True


def getMenuItemPrice (theDictionary, item):
    """Identifies the price of item.

    Assumes items are written in uppercase.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :param str item:
        The name of item to check the price of.
    :return:
        The price of item if in theDictionary, else None.
    :rtype: float or None
    """
    item = item.upper()

    if item in theDictionary:
        return theDictionary[item]


def averagePrice (theDictionary):
    """Identifies the average price of items on the menu.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :return:
        The average of all prices rounded to 2 decimal places.
    :rtype: float
    """
    prices = list(theDictionary.values())
    average = round(mean(prices), 2)

    return average


def takeOrder (theDictionary):
    """Create a mock order for a number of items from the menu.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :except ValueError:
        Quantities of items should be input as ints.
    :rtype:
    """
    # CAO 20220429
    btcRate = 0.000026
    orderItems = {}
    menuItems = list(theDictionary.keys())


    print("Welcome to Burger Hut! Here is our menu:")
    printMenu(theDictionary)
    print("\nEnter desired menu items when prompted."
          "Press \"Enter\" at the prompt to complete your order.")

    while True:
        if len(orderItems) == 0:
            order = input("What can I get started for you today? "
                          "").upper().strip()
        else:
            order = input("What else can I get for you? ").upper().strip()

        if order == "":
            break
        elif order not in theDictionary:
            comebacks = [
                f"{order} was a limited time item that we're not serving at "
                f"the moment.",
                f"{order} is not an item that we serve. How about a "
                f"{menuItems[randint(0, len(menuItems) - 1)]} instead?"
            ]

            print(comebacks[randint(0, len(comebacks) - 1)])
        else:
            while True:
                quantityPrompt = input("How may of those would you like? "
                                       "").strip()
                try:
                    quantity = int(quantityPrompt)
                    break
                except ValueError:
                    print(f"{quantityPrompt} is not a valid quantity.")


            if order not in orderItems:
                orderItems[order] = quantity
            else:
                orderItems[order] = orderItems[order] + quantity

    if len(orderItems) > 0:
        print("\nYour order:")
        for key, value in orderItems.items():
            numX = str(value) + "x"
            print(f"{numX:<3s} {key}")
        print()

        total = 0.0
        for item in orderItems:
            amount = orderItems[item] * theDictionary[item]
            total += amount
        btcTotal = total * btcRate

        print(f"Your total comes to ${total}.\n"
              f"We would also accept {btcTotal:.6f} Bitcoin.\n"
              f"How would you like to pay?")

    else:
        print("That person left without ordering anything. How strange....")


def printMenu (theDictionary):
    """Prints a table of menu items and prices.

    :param dict[str, float] theDictionary:
        Dict containing menu items as keys and respective prices as
        prices.
    :rtype: None
    """
    itemColumnWidth = 1
    priceColumnWidth = 1

    for key, value in theDictionary.items():
        if len(key) > itemColumnWidth:
            itemColumnWidth = len(key)
        if len(str(value)) > priceColumnWidth:
            priceColumnWidth = len(str(value))

    # + 1 to account for "$"
    priceColumnWidth += 1
    spacer = 4
    totalWidth = itemColumnWidth + priceColumnWidth + spacer

    menuItemsHeader = "Menu Items"
    priceHeader = "Price"
    print(
        menuItemsHeader +
        " " * (totalWidth - len(menuItemsHeader) - len(priceHeader)) +
        priceHeader
    )
    print("=" * totalWidth)

    for key, value in theDictionary.items():
        print(
            f"{key}" +
            # whole dollar amount is float w/ only 1x 0 after decimal
            "." * (totalWidth - len(key) - len(str(value)) - (
                # - 1 to account for "$"
                # - 2 to account for whole dollar amount + "$"
                1 if value % 1 != 0 else 2
            )) +
            f"${value:{priceColumnWidth - 3 }.2f}"
        )


def main():
    print("Enter name of data text file containing menu items and prices.")
    dataFile = promptTextFileRead()
    if not dataFile:
        print("Data file not found.\nExiting program.")
        exit()

    # testing readMenuItems
    print("Lets take a look at the menu.")
    menu = readMenuItems(dataFile)
    print(menu)
    print()

    # testing totalMenuItems
    total = totalMenuItems(menu)
    print(f"Total items on menu: {total}")
    print()

    # testing getMenuItems
    menuItems = getMenuItems(menu)
    print(f"Sorted list of menu items: {menuItems}")
    print()

    # testing getMenuItemsWithinRange
    ranges = [[5.99, 10.99], [8.99, 10.99], [1.99, 5.99]]

    for r in ranges:
        items = getMenuItemsWithinRange(menu, r[0], r[1])

        if len(items) > 0:
            print(f"List of menu items priced between ${r[0]} and ${r[1]}: "
                  f"{items}")
        else:
            print(f"There are no menu items priced between ${r[0]} and "
                  f"${r[1]}.")
    print()

    # testing takeOrder
    takeOrder(menu)
    print()

    # testing addMenuItem
    newMenuItems = {"beesechurger": 42.000001, "cheeseburger": 8.49}

    for key, value in newMenuItems.items():
        key = key.upper()
        value = round(float(value), 2)
        addedItem = addMenuItem(menu, key, value)

        if addedItem:
            print(f"{key} added to the menu for the price of ${value:.2f}.")
        else:
            print(f"{key} already exists on the menu.")

    print("New Menu:")
    print(menu)
    print()

    # testing updateMenuItem
    newMenuItems = {"beesechurger": 69.69, "chicken sandwich": 8.49}

    for key, value in newMenuItems.items():
        key = key.upper()
        value = round(float(value), 2)
        updatedItem = updateMenuItem(menu, key, value)

        if updatedItem:
            print(f"Updated price of {key} to ${value:.2f}.")
        else:
            print(f"{key} is not a menu item.")

    print("Updated Menu:")
    print(menu)
    print()

    # testing getMenuItemPrice
    itemsToPrice = [
        "cheeseburger",
        "mushroom swiss burger",
        "chicken sandwich"
    ]

    for item in itemsToPrice:
        price = getMenuItemPrice(menu, item)

        if price:
            print(f"The price of {item.upper()}: ${price}")
        else:
            print(f"{item.upper()} is not on the menu.")
    print()

    # testing averagePrice
    average = averagePrice(menu)
    print(f"The average price of items on the menu: ${average}")
    print()

    # testing printMenu
    printMenu(menu)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 12, Part 1
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    1. Ask for a number of menu items and their prices.
    2. Fill a dictionary with those items/prices.
    3. Prompt for a file name to write the dictionary to.
    4. Write the dictionary to the file with a tab character separating
    the keys and the values.

.. note::
    Function HEADERS are written according to convention established by
    assignment issuer, i.e., written in camelCase with whitespace
    between the function's name and its parameters. camelCase persists
    for declaration of variables for consistency. When a function is
    called, the absence of whitespace between a function's name and its
    arguments was judged to have no effect on performance; thus, such
    whitespace is excluded outside of function headers.

Functions:
    promptTextFileWrite ()
        - Prompts for desired text file name for use in write mode.
    writeDictToFile (theDictionary, fileName, delimiter="\t"):
        - Writes the contents of a theDictionary to fileName.
    addItemstoMenu (menu):
        - Prompts for menu items and prices to add to menu.

"""

from os.path import isfile


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
        fileName = input("Text file name: ").lower()
        if fileName[-4:] != ".txt":
            print("File name must include \".txt\" extension.")
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


def writeDictToFile (theDictionary, fileName, delimiter="\t"):
    """Writes the contents of a theDictionary to fileName.

    Writes one key/value pair per line within the file in format
    "KEY[delimiter]VALUE".

    Designed primarily for use with text files. Writing to other file
    types may have unintended consequences.

    :param dict theDictionary:
        The dict to write to fileName
    :param str fileName:
        The name of the file to write to
    :param str delimiter:
        The character by which to delimit keys from values when writing
        a line of data to fileName
    :rtype: None
    """
    with open(fileName, "w") as f:
        for key in theDictionary:
            f.write (f"{key}{delimiter}{theDictionary[key]}\n")


def addItemstoMenu (menu):
    """Prompts for menu items and prices to add to menu.

    :param dict menu:
        Menu items are keys; prices are values.
    :except ValueError:
        Prices must be floats or ints.
    :return:
        menu with any added menu items and prices
    :rtype: dict[str, float]
    """
    print("=== ADD MENU ITEMS ===\n"
          "Name an item to add to the menu and assign each item a price.\n"
          "To exit press \"Enter\" for item name.\n")

    while True:
        item = input("Item name: ").upper()
        assignPrice = True

        if item == "":
            return menu

        if item in menu:
            assignPrice = False
            print(f"{item} is an existing menu item. Its price is ${menu[item]}.")

            while True:
                overwrite = input(f"Change price of {item}? "
                                  f"(y/n): ").lower()
                if overwrite not in ["y", "yes", "n", "no"]:
                    print(f"{overwrite} is not a valid response.")
                elif overwrite in ["y", "yes"]:
                    assignPrice = True
                    break
                else:
                    break

        if assignPrice:
            while True:
                price = input(f"{item} price: $")
                validPrice = False

                try:
                    price = round(float(price), 2)

                    if price < 0:
                        print("A price cannot be negative.")
                    else:
                        validPrice = True

                    if validPrice:
                        menu[item] = price
                        break

                except ValueError:
                    print(f"{price} is not a valid price")






def main():
    menu = {}
    menu = addItemstoMenu(menu)
    fileName = promptTextFileWrite()
    writeDictToFile(menu, fileName)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

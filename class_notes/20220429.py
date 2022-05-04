"""
Java doesn't global variables
DON'T USE GLOBALS UNLESS IT IS VERY OBVIOUSLY A GOOD IDEA

What is a queue in programming?
Putting things in certain order to ensure desired functionality

global constants are fine because they never change
global VARIABLES are a very bad idea

Python encourages one logical line being one physical line

variable = [
    'string',
    'other string'
    ]

python has to see a function before it can call a function (at runtime)

VisualBasic has procedures of functions
    We're going to start with a "main" function
C started of calling a main, other languages followed

"""



def print_addresses(addresses):
    for address in addresses:
        print(address)


def listSortAscending (listToSort):
    """Sorts the contents of a list in ascending order.

    :param list listToSort: The items to be sorted.
    :raise TypeError:
        listToSort must be like items; cannot compare strings to
        ints/floats
    :rtype: None
    """
    # this index...
    for targetIndex in range (0, len (listToSort) - 1):
        # ...compared to this index
        for comparisonIndex in range (targetIndex + 1, len (listToSort)):
            if listToSort[targetIndex] > listToSort[comparisonIndex]:
                # target character
                temp = listToSort[comparisonIndex]
                # character moved into unsorted series
                listToSort[comparisonIndex] = listToSort[targetIndex]
                # target character moved into sorted position
                listToSort[targetIndex] = temp


"""
1. What to compare
2. The actual comparison
3. Swapping of values in list if needed

Eventually will get into recursion (while loop)

Do i leave them where they are or do I swap places w/in the list

The key is in the if statement. How do you want to do your comparison?

when sorting addresses you could split 1 time to separate the number from
the avenue

first you need to convert the number string to an int
"""


"""
We start with the basics (reinvent the wheel) so we have an understanding
of why and how. This allows us to be creative. Basic --> creative

"""
def main():
    addresses = [
        "2400 University Ave",
        "150 University Ave",
        "9 University Ave",
        "60 University Ave"
    ]

    print_addresses(addresses)


if __name__ == "__main__":
    main()





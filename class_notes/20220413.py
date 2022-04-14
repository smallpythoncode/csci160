"""
complex data structure: stores more than one value

lists vs dictionaries: how to know which one to use?
lists generally have like values (names, temperatures)
dictionaries work well with different types of values
(student name: student ID)

list have indexes --> indexes have implied meaning
what you do with one item, you do with all the items
not necessarily sorted since the indexes have meaning

dictionaries have keys
grocery list, but which would be the key, value?
it works, but why?
"""

"""
how many unique characters are there?

#### LAMBDAs are used in sorts
"""

str = "fjkldahljboho3ebka;ohboiaklehhajdkj"

uniqueList = []
uniqueDict = {}

# for list
for char in str:
    # this will change the data
    # be careful of changing data as index likely has meaning
    char = char.lower()
    # if char.isalpha(): # if we're only interested in a thru z
    if char > "a" and char <= "z":
        # could be if not char in uniqueList # check boolean
        # not is a built-in feature in Python
        # probably NOT in most other languages
        if char not in uniqueList:
            uniqueList.append(char)

# for dict
# adding is the same as updating
for char in str:
    char = char.lower()
    if char > "a" and char <= "z":
        uniqueDict[char] =
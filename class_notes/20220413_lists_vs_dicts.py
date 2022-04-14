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
# dicts are called hashes in other programming language
# hashes are covered in 161 (will use lists for this)
# key could be the same as the value
# value is just along for the ride
# what is a hash map in java?
for char in str:
    char = char.lower()
    if char > "a" and char <= "z":
        uniqueDict[char] = True
        # if printed, uniqueDict values would be True

"""
lists can be sorted, dicts cannot
dicts can be printed as sorted, but not properly sorted
The only way it can be is if it were created in order

pull the keys to a list, sort the list, print they dict by key order
"""

uniqueChars = list(uniqueDict.keys())
uniqueChars.sort()
for char in uniqueChars:
    print(char, end="")

# wipes the dict clean
uniqueDict.clear()

# track how many you have
for char in str:
    char.lower()
    if char >= "a" and char <= "z":
        # this will crash the program
        # trying to access something in the dict before putting
        # it in the dict is why
        # --> uniqueDict[char] = uniqueDict[char] + 1
        if char in uniqueDict:
            # this alone will crash since we're trying to access ( += )
            # something that doesn't exist
            uniqueDict[char] = uniqueDict[char] + 1  #updating
        # will initialize the value
        # only time where there is a literal
        # the one time we know for sure what the value will be
        # know when to distinguish between adding and updating
        else:
            uniqueDict[char] = 1  # adding

# lambda can be used to sort the value

uniqueChars = list(uniqueDict.keys())
# n is uniqueDict so we can get the value, ie. what we are trying to sort
uniqueChars.sort(key=lambda n: uniqueDict[n])
# will print ascending vs descending
uniqueChars.reverse()
# can be done with parallel lists if done with a counter

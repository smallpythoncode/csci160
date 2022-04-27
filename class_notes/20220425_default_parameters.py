"""
create a dictionary
dict_var = {}

keys are pseudo-variables
should be descriptive...should

valid_keys = ["Credits", "Major"]
if this is w/in the module, this would be global variable
generally, global variables are not a good idea

global constants however could be very useful
use as a tuple instead since they cannot be modified

in Java, the final keyword could in effect create a tuple
Python: vars = ("some string", "other string")
Java: final vars = ["some string", "other string"]
C++: const vars = ["some string", "other string"]

quick sort will be touched on in 161

abstraction - What goes on in the background without the user
necessarily knowing
obscuring of details
default parameters

"""

import os

valid_keys = ("credits", "major")




def add_info(advisees, name, credits, major):
    # what if name already exists?
    # used to add only if someone is new
    # something will need to be written to check if name already exists
    # code communicates with code via arguments, parameters, and returns
    # boolean returns are very common
    # how do we know if name exists?

    # how to tell the call that name is already in advisees?
    if name in advisees:
        return False
    else:
        advisees[name] = {}
        advisees[name]["credits"] = credits
        advisees[name]["major"] = major
        return True

def print_advisees(advisees):
    header = format("Name", "10s") + \
        format("Credits", "10s") + \
        format("Major", "10s")
    print(header)
    print("=" * len(header))

    advisee_names = list(advisees.keys())
    advisee_names.sort()
    for name in advisee_names:
        print(f"{name:10s}", end="")
        for key in advisees[name]:
            print(f"{str(advisees[name][key]):<10s}", end="")
        print()


def print_advisees_by_credits(advisees):
    header = format("Name", "10s") + \
        format("Credits", "10s") + \
        format("Major", "10s")
    print(header)
    print("=" * len(header))

    advisee_names = list(advisees.keys())
    # n is what is in the if statement for a lambda
    # without lambda, will sort by name
    # with lambda, chooses the if by which it is sorted
    # instead of if some_key less than other_key
    # searches by if ["credits"] by some_key is less than
    # ["credits"] by other_key
    advisee_names.sort(key=lambda n: advisees[n]["credits"])
    for name in advisee_names:
        print(f"{name:10s}", end="")
        for key in advisees[name]:
            print(f"{str(advisees[name][key]):<10s}", end="")
        print()


# build in options in how to sort
def print_advisees_with_sortfield(advisees, sort_field=None):
    advisee_names = list(advisees.keys())
    if sort_field is None:
        advisee_names.sort()
    else:
        advisee_names.sort(key=lambda n: advisees[n]["credits"])

    header = format("Name", "10s") + \
        format("Credits", "10s") + \
        format("Major", "10s")
    print(header)
    print("=" * len(header))

    for name in advisee_names:
        print(f"{name:10s}", end="")
        for key in advisees[name]:
            print(f"{str(advisees[name][key]):<10s}", end="")
        print()


def my_range(first, second=None, third=None):
    if second is None:
        start = 0
        stop = first
        step = 1
    elif third is None:
        start = first
        stop = second
        step = 1
    else:
        start = first
        stop = second
        step = third

    print("Print from ", start, " to ", stop, " by ", step, ".", sep="")



def main():
    # # contacts = {} #empty dictionary
    # fileName = "contacts.txt"
    # # contacts = {'Scott' : '7-1111', 'Tom' : '7-4107', 'UND SEECS' : '7-3337', 'Bob' : '7-5196'}
    # contacts = loadContacts(fileName)
    # if contacts == None:
    #     print("Bad data file, do whatever is right if there is no data file")
    #     exit()
    #
    # printContacts(contacts)
    # printSortedContacts(contacts)
    # printSortedContactsByNumber(contacts)
    # addContacts(contacts)
    #
    # saveContacts(fileName, contacts)

    advisees = {}
    # dict[key] = value
    # advisees["Tom"] = {"gpa": 2.0, "credits": 69}
    # advisees["Diego"] = {"gpa": 3.0, "credits": 42}
    advisees["Tom"] = {}
    advisees["Tom"]["credits"] = 69
    advisees["Tom"]["major"] = "CSCI"

    advisees["Espen"] = {}
    advisees["Espen"]["credits"] = 42
    advisees["Espen"]["major"] = "CSCI"

    info_added = add_info(advisees, "Max", 35, "Data Science")
    info_added = add_info(advisees, "Max", 35, "Data Science")


    print(advisees)

    print_advisees(advisees)
    print()
    print_advisees_by_credits(advisees)
    print()
    print_advisees_with_sortfield(advisees)

    print()
    my_range(10)
    my_range(1, 20)
    my_range(6, 90, 3)


main()
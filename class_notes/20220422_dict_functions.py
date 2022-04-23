"""
Remember - Quiz 5 is through ProctorU

contact list creation

we bring multiple dictionaries together?
if in a dict, what are the keys and what are the values?

if soring a dict of student information,
student ID would be most ideal since it is nearly impossible to
be identical with another student

key could be id value could other student info (gpa, credits, etc)

"""

import os

# not needed
# look for first "needed" comment
def printContacts(contacts):
    contactWidth = "10"
    numberWidth = "11"
    print(format("Contact", contactWidth + "s"),
          format("Number", numberWidth + "s"))
    print("-" * int(contactWidth), "-" * int(numberWidth))
    for contact in contacts:
        print(format(contact, contactWidth + "s"),
              format(contacts[contact], numberWidth + "s"))
    print()


def printSortedContacts(contacts):
    contactWidth = "10"
    numberWidth = "11"
    sortedContacts = list(contacts.keys())
    sortedContacts.sort()
    print(format("Contact", contactWidth + "s"),
          format("Number", numberWidth + "s"))
    print("-" * int(contactWidth), "-" * int(numberWidth))
    for contact in sortedContacts:
        print(format(contact, contactWidth + "s"),
              format(contacts[contact], numberWidth + "s"))
    print()


def printSortedContactsByNumber(contacts):
    contactWidth = "10"
    numberWidth = "11"
    sortedContacts = list(contacts.keys())
    sortedContacts.sort(key=lambda n: contacts[n])
    print(format("Contact", contactWidth + "s"),
          format("Number", numberWidth + "s"))
    print("-" * int(contactWidth), "-" * int(numberWidth))
    for contact in sortedContacts:
        print(format(contact, contactWidth + "s"),
              format(contacts[contact], numberWidth + "s"))
    print()


def addContacts(contacts):
    contactToAdd = input("Enter contact to add - press ENTER to quit: ")
    while contactToAdd != "":
        numberToAdd = input("Enter number for " + contactToAdd + ": ")
        # add to dictionary
        if contactToAdd in contacts:
            overwriteEntry = input(
                contactToAdd + " already exists, overwrite (y/n)? ")
            if overwriteEntry.lower().strip()[0] == 'y':
                # if overwriteEntry.lower().strip()[0] != 'n':
                contacts[contactToAdd] = numberToAdd
        else:
            contacts[contactToAdd] = numberToAdd

        contactToAdd = input("Enter next contact to add: ")


def saveContacts(fileName, contacts):
    outFile = open(fileName, "w")
    for contact in contacts:
        outFile.write(contact + "\t" + contacts[contact] + "\n")
    outFile.close()


def loadContacts(fileName):
    if not os.path.isfile(fileName):
        return None
    contacts = {}
    inFile = open(fileName, "r")
    for line in inFile:
        line = line.strip()
        contact, number = line.split('\t')
        contacts[contact] = number

    return contacts


# first needed function for this lecture
# approach how functions are written like I am writing the function
# but somebody else is writing main()
# if something is needed to make a function run, put it as a parameter
# don't make assumptions of what the user thinks they will need
# tell them what they will need
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
main()
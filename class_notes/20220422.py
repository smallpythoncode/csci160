"""
Remember - Quiz 5 is through ProctorU

contact list creation

"""

import os


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


def main():
    # contacts = {} #empty dictionary
    fileName = "contacts.txt"
    # contacts = {'Scott' : '7-1111', 'Tom' : '7-4107', 'UND SEECS' : '7-3337', 'Bob' : '7-5196'}
    contacts = loadContacts(fileName)
    if contacts == None:
        print("Bad data file, do whatever is right if there is no data file")
        exit()

    printContacts(contacts)
    printSortedContacts(contacts)
    printSortedContactsByNumber(contacts)
    addContacts(contacts)

    saveContacts(fileName, contacts)


main()
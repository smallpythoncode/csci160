"""
Quiz 6 will happen during finals week

"""

from os.path import isfile

contact_list = {"Bob": "936", "Jahnke": "956", "Buck": "966"}

# print in sorted order
# keys are values
# .keys() puts keys of dict in a list

d = {"a": 1, "b": 2, "c": 3}
# a dict can be called a parallel array
# two lists that run along concurrently
d.keys()
print(d.keys())
# converts the keys into a list object variable
bunky = list(d.keys())
print(bunky)

# this is the fundamental version of .keys()
# what the method does essentially (built-in)
d_list = []
for key in d:
    d_list.append(key)

print(d_list)

# .keys() method can be used to sort (i.e print as sorted) a dict

"""
to print sorted
for contact in sorted_contacts:
    print(format(contact), format(sorted_contact[contact]))

"""

# lambda functions


def print_sorted_contacts_by_number(contacts):
    # lambda gives us the ability to control how the sort works
    # in this case n can be any variable our heart desires
    # n is just the most commonly used
    sorted_contacts = list(contacts.keys())
    # must be part of the sort, the last line puts in list, doesn't sort
    # # we sort by number here
    # where standard sort would put in order by key (alphabetically)
    # the lambda allows us to "interject" into the sort by pulling
    # the number (contacts[n]) and use that as the "if" in the sort
    sorted_contacts.sort(key=lambda n: contacts[n])


def save_contacts(file_name, contacts):
    # if worried about overwriting a file, file_name would
    # be necessary
    # same if you were reading a file
    # but to just create a new file (or overwrite), file_name
    # wouldn't be necessary
    # in the context of fileUtils especially

    # when working with .txt, don't do "w+" or any other plus
    # BAD IDEA
    # counting on newline character being there
    # "+" would only really be valuable for binary files

    # can also be written w/ context manager (with open)
    out_file = open(file_name, "w")
    for contact in contacts:
        # don't forget the \n !!!
        out_file.write(contact + "\t" + contacts[contact] + "\n")
    out_file.close()

    # tabs generally work every 8 columns

# VERIFY
def load_contacts(file_name):
    contacts = {}
    if not isfile(file_name):
        return None

    in_file = open(file_name, "r")
    for line in in_file:
        line = line.strip()
        contact, number = line.split("\t")
        contacts[contact] = number

    return contacts




"""
3 components to every sort
1. code that decides what items to compare
2. code that swaps items around (in-place if need be)
3. the decision (if statement)

for lambda functions, the n allows us to decide what is in the if
statement
"""


random_list = ["e", "B", "D", "c", "a"]
print(random_list)
random_list.sort()
print(random_list)

# sort so case doesn't matter
random_list.sort(key=lambda n: n.lower())
print(random_list)
# changes how you look at the value in the list
# doesn't change the value itself
# lambdas can be "lenses"

file_name = "contacts.txt"
contacts = load_contacts(file_name)
if contacts == None:
    print("Data file does not exist")
    # nothing to manipulate, nothing left for program to do, exit
    exit()


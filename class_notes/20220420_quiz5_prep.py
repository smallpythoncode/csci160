"""
quiz 5 is available thu through sat
lists and formatted output

for loop
something that changes the values in the list

methods for list
append
sort
key = lambda WON'T be on quiz
indexes will be on quiz

l = [3, 5, 9, 6, 2]
for i in range(0, 3):
    l[i] = l[i + 2] + 10
print(l)

all strings have the exact same functionality
"""

"""
use any formatting method
(format) for f-strings

name = "Tom"
age = 39
balance = 3.14
                  1                   2                   3
1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
T o m             3 9             3 . 1 4

Write something that generates formatted with this spacing
 
variables could be anything

"""

name = "Jahnke"
age = 30
pi = 3.14

g = f"{name:<8s}{age:>3d}{pi:>10.2f}"
print(g)
print(len(g))
# or
print(format(name, "8s"), format(age, ">3d"), format(pi, ">10.2f"), sep="")
# other method (old) print("%8s%3d%10.2f"%(name, age, pi)
# I don't like this method because there's not obvious way to justify

"""
QUIZ KEY TAKE AWAYS
list, format, output, indexes
"""
"""
finals week quiz will be on dictionaries

what can be a key?
Any single value can be a key
Try for strings or ints
CAN be floats, but generally a bad idea since a float is an approximation
can be a bool, but that limits the keys to only a value of 2

values can be anything that can be put into a variable
not all values have to be of the same type
- not advised necessarily, because they key should (emphasis)
  be all the same type
  why?
  to manipulate the data
  grouping different types together would decrease the ability
  to utilize that data


how do we build a data structure
strings, dicts, lists

create complexity by adding layers

think of creating a contact in your phone
how to store information?

create a dictionary template with first name, last name, number, etc.

how do we have a collection of dictionaries? lists? dictionaries?

how do you know if you have a list or dictionary?
depends on how you can access it

do you have a key? you have a dict
there is no first key or second key, etc
there are only keys

this differentiates dicts from lists
"""


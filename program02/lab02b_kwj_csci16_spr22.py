"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160 - Spring 2022
Lab 2 Part B

Prompt for a user's first name, last name, street address, city, state,
and ZIP code.
Print this information using this format:
<first name> <last name>
<street address>
<city>, <state> <zip code>

Challenge:
1. Print using the format described above.
2. Print the format using a single print statement.
3. Print the format using six print statements.
"""

# prompts
first_name = input("First name: ").title()
last_name = input("Last name: ").title()
# street_address will output NE or SW incorrectly
# could an if-statement be added to detect NE or SW and upper the result?
street_address = input("Street address: ").title()
us_states = ["AL", "AK", "AZ", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
             "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI",
             "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
             "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
             "VT", "VA", "WA", "WV", "WI", "WY"]
city = input("City: ").title()
state = input("State: ").upper()
while state not in us_states:
    state = input("State (2-character postal abbreviation): ").upper()
zip_code = input("ZIP Code: ")
while len(zip_code) != 5 or not isinstance(int(zip_code), int):
    zip_code = input("ZIP Code (5-digit): ")

# empty print statement added to end of each challenge for aesthetics
# challenge 1
print(first_name, last_name)
print(street_address)
print(city, ", ", sep="", end="")
print(state, zip_code)
print("")

# challenge 2
print(first_name, " ", last_name, "\n", street_address, "\n", city, ", ",
      state, " ", zip_code, sep="")
print("")

# challenge 3
print(first_name, end=" ")
print(last_name)
print(street_address)
print(city, end=", ")
print(state, end=" ")
print(zip_code)

# All work and no play makes Jack a dull boy.

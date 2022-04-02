"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Lab 09

"""

from random import choice


def reverse_by_index(string):
    """Reverses a string via indexing.

    :param string: The string to be reversed
    :type string: str
    :return: string reversed
    :rtype: str
    """
    reverse_string = string[::-1]

    return reverse_string


def reverse_via_join(string):
    """Utilizes the join and reversed methods to reverse a string.

    :param string: The string to be reversed
    :type string: str
    :return: string reversed
    :rtype: str
    """
    reverse_string = "".join(reversed(string))

    return reverse_string


def reverse_via_for_loop(string):
    """Reverses a by iterating through string.

    :param string: The string to be reversed
    :type string: str
    :return: string reversed
    :rtype: str
    """
    reverse_string = ""
    for char in range(len(string) - 1, -1, -1):
        reverse_string += string[char]

    return reverse_string


def palindrome_check(string):
    """Checks if string is a palindrome.

    Checks if even or odd palindromes or neither.
    Randomly selects a function to make the determination.

    :param string: The string to be checked
    :type string: str
    :return: The palindrome determination and the function used
    :rtype: tuple
    """
    reverse_functions = [
        reverse_by_index,
        reverse_via_join,
        reverse_via_for_loop
    ]
    random_reverse = choice(reverse_functions)
    reverse_string = random_reverse(string)

    if string == reverse_string:
        if len(string) % 2 == 0:
            return random_reverse.__name__, "an even palindrome"
        else:
            return random_reverse.__name__, "an odd palindrome"
    else:
        return random_reverse.__name__, 



"""
while True:
    string = input("Enter")
    if string == "":
        break
    else:
        reverse_string = string[::-1]
        if string == reverse_string:
            if len(string) % 2 == 0:
                return "Even"
            else:
                return "Odd
        else:
            return "Not Palindrome



"""



def prompt_palindrome_string():
    """A simple prompt to be used for checking palindromes.

    :return: The string to be checked as a palindrome
    :rtype: str
    """
    string = "Enter to a string to check if it is a palindrome: "

    return string



def main():
    print(palindrome_check("boob"))


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Lab 09

Create a module that prompts the user for a string and checks if that
string is a palindrome.

Functions:

    reverse_by_index(string)
        Reverses a string via indexing.
    reverse_via_join(string)
        Utilizes the join and reversed methods to reverse a string.
    reverse_via_for_loop(string)
        Reverses a by iterating through string.
    palindrome_check(string, return_function=True)
        Checks if string is a palindrome.
    prompt_palindrome_string()
        A simple prompt to be used for checking palindromes.
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


def palindrome_check(string, return_function=True):
    """Checks if string is a palindrome.

    Checks if even or odd palindromes or neither.
    Randomly selects a function to make the determination.

    :param string: The string to be checked
    :type string: str
    :param return_function: The choice to return reversal function name
    :type return_function: bool
    :returns:
        if return_function:
            Palindrome determination & string reversal function name
        else:
            Palindrome determination
    :rtype: tuple or str
    """
    reverse_functions = [
        reverse_by_index,
        reverse_via_join,
        reverse_via_for_loop
    ]
    random_reverse = choice(reverse_functions)
    reverse_string = random_reverse(string)

    if return_function:
        if string == reverse_string:
            if len(string) % 2 == 0:
                return random_reverse.__name__, "an even palindrome"
            else:
                return random_reverse.__name__, "an odd palindrome"
        else:
            return random_reverse.__name__, "not a palindrome"
    else:
        if string == reverse_string:
            if len(string) % 2 == 0:
                return "an even palindrome"
            else:
                return "an odd palindrome"
        else:
            return "not a palindrome"


def prompt_palindrome_string():
    """A simple prompt to be used for checking palindromes.

    :return: The string to be checked as a palindrome
    :rtype: str
    """
    string = input("Enter to a string to check if it is a palindrome: ")

    return string


def main():
    print("PALINDROME CHECKER\nTo exit, enter an empty string.\n")

    while True:
        prompt = prompt_palindrome_string()
        if prompt == "":
            break
        else:
            result = palindrome_check(prompt)
            print("Checking for palindrome using ", result[0], "().", sep="")
            print("\"", prompt, "\"", " is ", result[1], ".\n", sep="")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

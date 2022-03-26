"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 08, Part 1

1. Prompt the user for floating point numbers until "-1" is entered.
2. Add each valid value to a list.
3. Prompt the user for a file name.
4. Write each value to the file, one value per line.

Functions:

    prompt_floats()
        Prompts user for floats to be added to a list.
    prompt_txt_file_name():
        Prompts user for desired name of .txt file.
    write_list_to_file(target_list, file):
        Writes elements of a list to a file, one element to a line.
"""

from os.path import isfile


def prompt_floats():
    """Prompts user for floats to be added to a list.

    Prompting ends when "-1" is entered.

    :return: A list containing the floats entered.
    :rtype: list
    :raise ValueError: Only floats or ints may be entered
    """
    print("Enter floating point numbers.")
    print("To end, enter \"-1\"")
    floats = []
    prompt = input("Number: ")
    while prompt != "-1":
        try:
            num = float(prompt)
            floats.append(num)
            prompt = input("Number: ")
        except ValueError:
            print("Invalid data type. Entry rejected."
                  "")
            prompt = input("Number: ")
    return floats


def prompt_txt_file_name():
    """Prompts user for desired name of .txt file.

    Currently does not check for other file types.

    :return: The name of a .txt file
    :rtype: str
    """
    while True:
        # if necessary, add extensions to list and check containment
        extension = ".txt"
        file_name = input("Enter desired file name. Do not add a file "
                          "extension.\nFile name: ")
        if extension not in file_name:
            file_name = file_name + ".txt"
            break

    return file_name


def write_list_to_file(target_list, file):
    """Writes elements of a list to a file, one element to a line.

    If the file already exists, user is asked if file is to be
    overwritten.

    :param target_list: The list of integers to be written line-by-line
    :type target_list: list
    :param file: The file to be written to
    :type file: str
    :return: None
    """
    if isfile(file):
        yes = ["y", "yes"]
        no = ["n", "no"]
        print()
        print(f"{file} already exists.")
        while True:
            overwrite = input("Do you wish to ovewrite? (y/n): ").lower()
            if overwrite in no:
                break
            elif overwrite in yes:
                with open(file, "w") as f:
                    for value in target_list:
                        f.write(str(value) + "\n")
                break
    else:
        with open(file, "w") as f:
            for value in target_list:
                f.write(str(value) + "\n")


def main():
    floats = prompt_floats()
    print()
    file = prompt_txt_file_name()
    write_list_to_file(floats, file)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

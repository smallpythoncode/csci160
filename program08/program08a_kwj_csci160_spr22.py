"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 08, Part 1

1. Prompt the user for floating point numbers until "-1" is entered.
2. Add each valid value to a list.
3. Prompt the user for a file name.
4. Write each value to the file, one value per line.

Functions:



"""


def prompt_floats():
    """Prompts user for floats to be added to a list "floats".

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
            print("INVALID DATA TYPE")
            prompt = input("Number: ")
    return floats


def write_list_to_file(target_list):
    """Writes elements of a list to a new file, one element to a line.

    :param target_list: The list of integers to be written line-by-line
    :type target_list: list
    :return: None
    """
    while True:
        # if necessary, add doubles to list and scan w/ for loop
        double_extension = ".txt"
        file_name = input("Enter desired file name. Do not add a file "
                          "extension.\nFile name: ")
        if double_extension not in file_name:
            file_name = file_name + ".txt"
            break

    with open(file_name, "w") as file:
        for value in target_list:

            file.write(str(value) + "\n")


def main():
    # floats = prompt_floats()
    # print(floats)
    deez = [1, 2, 3]
    write_list_to_file(deez)



if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 07

# TODO: Write premise of assignment

Functions:

    transaction_type() # TODO: list parameters
        # TODO: summary
    _read_data() # TODO: list parameters
        # TODO: summary
    # TODO: List functions


"""

from os.path import isfile
import datetime


def get_data_file():
    while True:
        df = input("Enter name of checking account data file: ")
        if df == "exit":
            raise SystemExit
        elif not isfile(df):
            print("\tFile \"" + df + "\" does not exist.")
            print("\tEnsure correct spelling and file extensions.")
            print("\tEnter \"exit\" to exit program.")
        else:
            break

    return df




# TODO: TUPLE: trans_type, date, amount = something.split(",")

# TODO: strip method and split method


def display_data(data_file):
    with open(data_file) as reader:
        for line in reader:
            trans_type, date, amount = line.split(",")
            print(trans_type, date, amount, end="")





def transaction_type():
    pass


def main():
    df = "checking_account_data.txt"
    # df = get_data_file()

    display_data(df)


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

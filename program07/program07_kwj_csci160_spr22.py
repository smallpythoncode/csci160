"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 07

Print the contents of a text file containing checking account data of
prescribed format to a formatted table with date, type of transaction,
transaction amount, and running balance.

Functions:

    get_data_file()
        Prompts the user for the checking account data file name.
    data_verification(df):
        Ensures that the data within the file is valid.
    trans_type(code):
        Translates transaction code for human readability.
    display_balance_today():
        Notifies the user of the balance as of today.
    balance_movement(current_balance, trans_code, trans_amount):
        Adjusts the current balance based on the transaction type.
    figure_format(figure):
        Takes a dollar figure and formats it with commas.

Developer Notes:

    This program could be improved slightly by adding +/- to the
    transaction amount.
"""

from os.path import isfile
import datetime as dt


def get_data_file():
    """Prompts the user for the checking account data file name.

    :return: Name of data file (if valid)
    :raise SystemExit: If name of data file does not exist, user is
        prompted to try again or type "exit"
    """
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


def data_verification(df):
    """Ensures that the data within the file is valid.

    :param df: The data file to be verified
    :type df: str
    :return: True if data is valid, False if not
    :rtype: bool
    :raise ValueError: Line of data must only contain
        comma-separated transaction code, transaction date, then
        transaction amount
    """

    def trans_code_verification(code):
        """Ensure first element of data is a valid transaction code.

        :param code: Single-letter uppercase code for transaction type
        :type code: str
        :return: True if code is valid, False if not
        :rtype: bool
        """

        valid_codes = ["B", "C", "D", "W"]
        if code not in valid_codes:
            return False
        else:
            return True

    def trans_date_verificiation(date):
        """Ensure second element of data is a valid transaction date.

        :param date: Date of transaction (MM/DD)
        :type date: str
        :return: True if date is valid, False if not
        :rtype: bool
        :raise ValueError: Date is invalid
        """
        month, day = date.split("/")
        try:
            verify_date = dt.date(dt.date.today().year, int(month), int(day))
            return True
        except ValueError:
            return False

    def trans_amount_verification(amount):
        """Ensure third element of data is a valid transaction amount.

        Must include decimal. Must be at least 4 characters. Must be
        2 places for cents.

        :param amount: Amount of transaction
        :type amount: str
        :return: True if amount is valid, False if not
        :rtype: bool
        :raise ValueError: amount cannot be converted to float
        :raise ValueError: No decimal present in string
        """
        try:
            float_amount = float(amount)
        except ValueError:
            return False
        try:
            dollars, cents = amount.split(".")
        except ValueError:
            return False
        if amount.find(".") == -1 or len(amount) < 4 or len(cents) != 2:
            return False
        else:
            return True

    with open(df) as reader:
        for line in reader:
            try:
                trans_code, trans_date, trans_amount = line.split(",")
                valid_code = trans_code_verification(trans_code)
                valid_date = trans_date_verificiation(trans_date)
                valid_amount = trans_amount_verification(trans_amount.strip())

                if not (valid_code and valid_date and valid_amount):
                    return False
            except ValueError:
                return False

    return True


def trans_type(code):
    """Translates transaction code for human readability.

    :param code: The code to be converted
    :type code: str
    :return: Human-readable transaction type
    :rtype: str
    """
    if code == "B":
        return "Beginning Balance"
    if code == "C":
        return "Check"
    if code == "D":
        return "Deposit"
    if code == "W":
        return "Withdrawal"


def display_balance_today():
    """Notifies the user of the balance as of today.

    :return: Date balance is checked
    :rtype: str
    """
    today = dt.datetime.today().strftime("%m/%d")
    return f"BALANCE AS OF {today}"


def balance_movement(current_balance, trans_code, trans_amount):
    """Adjusts the current balance based on the transaction type.

    :param current_balance: The starting balance of the transaction
    :type current_balance: str
    :param trans_code: The type of transaction
    :type trans_code: str
    :param trans_amount: The amount of the transaction:
    :type trans_amount: str
    :return: The updated balance after the transaction
    :rtype: str
    """

    if trans_code in ["C", "W"]:
        return str(round(float(current_balance) - float(trans_amount), 2))
    elif trans_code == "D":
        return str(round(float(current_balance) + float(trans_amount), 2))
    else:
        return trans_amount


def figure_format(figure):
    """Takes a dollar figure and formats it with commas.

    :param figure: The figure to be formatted
    :return: The figure formatted with commas in appropriate places
    :rtype: str
    :raise ValueError: figure must contain a decimal to split str
    :raise ValueError: figure must be at least 4 chars in 'D.CC' format
    :raise AttributeError: figure must be a string
    """
    if len(figure) < 4:
        raise ValueError("figure must be at least 4 characters in "
                         "D.CC format")
    dollars, cents = figure.split(".")

    no_format = dollars
    with_format = ""
    while len(no_format) > 3:
        no_format = no_format[:len(no_format) - 3] + "," +\
                    no_format[len(no_format) - 3:]
        left, right = no_format.split(",")
        if len(with_format) == 0:
            with_format = right
        else:
            with_format = right + "," + with_format
        no_format = left

    if len(no_format) > 0 and len(with_format) == 0:
        formatted_figure = no_format + "." + cents
    elif len(no_format) > 0:
        formatted_figure = no_format + "," + with_format + "." + cents
    else:
        formatted_figure = with_format + "." + cents

    return formatted_figure


def main():
    df = get_data_file()
    df_is_valid = data_verification(df)
    if df_is_valid:
        print()
        print(display_balance_today())
        print()
        with open(df) as reader:
            current_balance = "0.00"
            for line in reader:
                trans_code, trans_date, trans_amount = line.split(",")
                trans_amount = trans_amount.strip()
                current_balance = balance_movement(current_balance,
                                                   trans_code, trans_amount)
                print(
                    f"{trans_date:7}",
                    f"{trans_type(trans_code):19}",
                    f"{figure_format(trans_amount):>12}"
                    f"{figure_format(current_balance):>15}"
                )
    else:
        print("Checking account data file is invalid.")
        print("Ensure data types and formatting are correct.")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

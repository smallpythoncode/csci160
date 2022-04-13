"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Project 02
Copyright (C) 2022 Kenneth Jahnke

Write and test each of the required functions per instructions for
CS160 Computer Science I, Project 2, Spring 2022

Required Functions:

    readTempData (fileName)
        Reads temperature information for a given month from data file.
    dailyHigh (highTemps, date)
        Finds the high temperature for date in question.
    dailyLow (lowTemps, date)
        Finds the low temperature for date in question.
    biggestDailyDifference (highTemps, lowTemps)
        Identifies the biggest difference in daily temperature.
    dayOfBiggestDailyDifference (highTemps, LowTemps)
        Identifies the day of the biggest difference in temperature.
    smallestDailyDifference (highTemps, lowTemps)
        Identifies the smallest difference in daily temperature.
    dayOfSmallestDailyDifferece (highTemps, lowTemps)
        Identifies the day of the smallest difference in temperature.
    monthlyAverage (temps)
        Calculates the average for a list of temperatures.
    biggestDifferenceBetweenDays (temps)
        Returns days w/ largest temp. difference compared to next day.
    printTemps (monthYearInfo, highTemps, lowTemps)
        Prints temperature data for target month.
    main()
        Tests at least all of the required functions.

Discretionary Functions:

    absoluteValue (value)
        Calculates the absolute value for a given value.
    dataAvailable (date, databaseList, dataAvailability)
        Checks that there is some data available for the queried date.
    dateFormattingAnchor (date)
        Aids in ensuring date format is correct by checking for comma.
    dateValidation (date)
        Verifies that a date is valid and formatted correctly.
    promptTempsDataFileName ()
        Prompts user for name of data file containing temperature data.
"""

from os.path import isfile


def readTempData (fileName):
    """Reads temperature information for a given month from data file.

    :param str fileName: The file containing high/low temperature data
    :raises IndexError: Excessive blank lines found w/in data file
    :except IndexError: Returns None if line is missing data elements
    :return:
        - (tuple) The month, year of the data
        - (list) The high temperatures
        - (list) The low temperatures

    """

    with open(fileName) as f:
        monthYearAssigned = False
        highTemps = []
        lowTemps = []
        for line in f:
            if not monthYearAssigned:
                monthYear = tuple(line.split())
                monthYearAssigned = True
            else:
                try:
                    highTemps.append(int(line.split(",")[1]))
                    lowTemps.append(int(line.split(",")[2]))
                except IndexError:
                    return None

    if len(monthYear) == 2:
        return monthYear, highTemps, lowTemps


def dailyHigh (highTemps, date):
    """Finds the high temperature for date in question.

    .. warning:
        Assumes date has been validated using dateValidation and that data
        exists for date in question using dataAvailable.

    :param list highTemps: High temperatures for given month
    :param date: Date (Month, day, year) to check for high temperatures
    :type date: list[str, str, str]
    :except IndexError: No data available for date in question
    :return: The high temperature for date
    :rtype: int or None
    """
    if date is not None:
        try:
            return highTemps[int(date[1]) - 1]
        except IndexError:
            return None


def dailyLow (lowTemps, date):
    """Finds the low temperature for date in question.

    .. warning:
        Assumes date has been validated using dateValidation and that data
        exists for date in question using dataAvailable.

    :param list lowTemps: Low temperatures for given month
    :param date: Date (Month, day, year) to check for low temperatures
    :type date: list[str, str, str]
    :except IndexError: No data available for date in question
    :return: The low temperature for date
    :rtype: int or None
        """
    if date is not None:
        try:
            return lowTemps[int(date[1]) - 1]
        except IndexError:
            return None


def biggestDailyDifference (highTemps, lowTemps):
    """Identifies the biggest difference in daily temperature.

    :param highTemps: Highs
    :param lowTemps: Lows
    :return: The biggest daily temp. difference for target month.
    :rtype: int
    """
    biggestDifference = -1
    if len(highTemps) == len(lowTemps):
        for i in range(len(highTemps)):
            currentDifference = highTemps[i] - lowTemps[i]
            if currentDifference > biggestDifference:
                biggestDifference = currentDifference

    return biggestDifference


def dayOfBiggestDailyDifference (highTemps, lowTemps):
    """Identifies the day of the biggest difference in temperature.

    :param list highTemps: Highs
    :param list lowTemps: Lows
    :return: Days of biggest difference in daily temp. for target month
    :rtype: list[int]
    """
    days = []
    biggestDifference = biggestDailyDifference(highTemps, lowTemps)
    if len(highTemps) == len(lowTemps):
        for i in range(len(highTemps)):
            if (highTemps[i] - lowTemps[i]) == biggestDifference:
                days.append(i + 1)

    return days


def smallestDailyDifference (highTemps, lowTemps):
    """Identifies the smallest difference in daily temperature.

    :param highTemps: Highs
    :param lowTemps: Lows
    :return: The smallest daily temp. difference for target month.
    :rtype: int
    """
    smallestDifference = 999999999999999999999999999999999999999999999999999999
    if len(highTemps) == len(lowTemps):
        for i in range(len(highTemps)):
            currentDifference = highTemps[i] - lowTemps[i]
            if currentDifference < smallestDifference:
                smallestDifference = currentDifference

    return smallestDifference


def dayOfSmallestDailyDifferece (highTemps, lowTemps):
    """Identifies the day of the smallest difference in temperature.

    :param list highTemps: Highs
    :param list lowTemps: Lows
    :return: Days of smallest difference in daily temp. for target month
    :rtype: list[int]
    """
    days = []
    smallestDifference = smallestDailyDifference(highTemps, lowTemps)
    if len(highTemps) == len(lowTemps):
        for i in range(len(highTemps)):
            if (highTemps[i] - lowTemps[i]) == smallestDifference:
                days.append(i + 1)

    return days


def monthlyAverage (temps):
    """Calculates the average for a list of temperatures.

    :param list temps: The temps of which to find the average
    :return: The average of temps
    :rtype: float
    """
    total = 0
    for i in range(len(temps)):
        total += temps[i]

    return total / len(temps)


def biggestDifferenceBetweenDays (temps):
    """Returns days w/ largest temp. difference compared to next day.

    :param list temps: Days to compare temperatures
    :return: list[int]
    """
    days = []
    biggestDifference = -1
    for i in range(len(temps) - 1):
        comparison = absoluteValue(temps[i] - temps[i + 1])
        if comparison > biggestDifference:
            biggestDifference = comparison
            days.clear()
            days.append(i + 1)
        elif comparison == biggestDifference:
            days.append(i + 1)

    return days


def printTemps (monthYearInfo, highTemps, lowTemps):
    """Prints temperature data for target month.

    :param monthYearInfo: Target month
    :type monthYearInfo: tuple(str, str)
    :param list highTemps: The high temps. for target month
    :param list lowTemps: The low temps. for target month
    :return: None
    """
    print(f"Temperature Data for {monthYearInfo[0]} {monthYearInfo[1]}")
    print("{:<} | {:>4} | {:>4}".format("Day", "High", "Low"))
    print("=" * 16)
    for i in range(len(highTemps)):
        print(f"{i + 1:<3} | {highTemps[i]:>4} | {lowTemps[i]:>4} ")


# discretionary
def absoluteValue (value):
    """Calculates the absolute value for a given value.

    :param value: The value to be calculated
    :return: The absolute value of value
    :rtype: int
    """
    if value < 0:
        return value * -1

    return value


# discretionary
def dataAvailable (date, databaseList, dataAvailability):
    """Checks that there is some data available for the queried date.

    .. warning:
        Assumes date has been validated using dateValidation.

    :param date: The queried date
    :type date: list[str, str, str]
    :param databaseList: List of months/years for which data is available
    :type databaseList: list[tuple]
    :param list dataAvailability: Determines range of dates available for
        month/year in question
    :return: date, if valid
    :rtype: list[str, str, str] or None
    """
    if date is not None:
        monthToCheck = date[0], date[2]
        availability = 1 <= int(date[1]) <= len(dataAvailability)
        if monthToCheck in databaseList and availability:
            return date


# discretionary
def dateFormattingAnchor (date):
    """Aids in ensuring date format is correct by checking for comma.

    .. note::
        Integral to dateValidation as of current version; subject to change.

    :param str date: The date string which should be in MMMM DD, YYYY format.
    :return: The index of the fist comma or -1 if none is found
    :rtype: int
    """
    comma = -1
    for i in range(len(date)):
        if date[i] == ",":
            comma = i
            break

    return comma


# discretionary
def dateValidation (date):
    """Verifies that a date is valid and formatted correctly.

    :param str date: Format: MMMM DD, YYYY (e.g., March 01, 2022)
    :except ValueError: Will return None if DD or YYYY is not able to be
        copied as integer
    :return: ["MMMM", "DD", "YYYY"]
    :rtype: list[str, str, str]
    """
    if dateFormattingAnchor(date) == -1:
        return None

    dateToValidate = date.split()
    # [Month[str], day[str], year[str]]
    if len(dateToValidate) != 3:
        return None
    dateToValidate = [i.strip(",") for i in dateToValidate]
    dateToValidate[0] = dateToValidate[0].title()
    # ensures 2-character day
    if len(dateToValidate[1]) != 2:
        return None
    try:
        for i in range(1, 3):
            int(dateToValidate[i])
    except ValueError:
        return None

    daysInMonths = {
        "January": 31,
        "February": {"standardYear": 28, "leapYear": 29},
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    if dateToValidate[0] in daysInMonths:
        if dateToValidate[0] == "February":
            if int(dateToValidate[2]) % 4 == 0:
                if 1 <= int(dateToValidate[1]) <= \
                        daysInMonths[dateToValidate[0]]["leapYear"]:
                    return dateToValidate
            else:
                if 1 <= int(dateToValidate[1]) <= \
                        daysInMonths[dateToValidate[0]]["standardYear"]:
                    return dateToValidate
        # if day is in range of days for target month
        elif 1 <= int(dateToValidate[1]) <= daysInMonths[dateToValidate[0]]:
            return dateToValidate


# discretionary
def promptTempsDataFileName ():
    """Prompts user for name of data file containing temperature data.

    Must include file extension, e.g., .txt.
    Data format contract:
        - Line 1: "Month Year", e.g., "March 2022"
        - Line 2 - Line n. 'Day,HighTemp,LowTemp', e.g., "10,69,30"

    .. warning::
        Excessive blank lines within (> 0) or at end of data (> 1) may
        cause exceptions if data file is argument of certain functions.

    :return: The temperature data file name if file exists
    :rtype: str or None
    """
    while True:
        fileName = input(
            "Enter name of temperature data file (include extension): ")
        if isfile(fileName):
            return fileName
        elif fileName == "":
            break
        else:
            print(f"{fileName} does not exist.\n"
                  "Try entry again or press 'Enter'.")


# tests functions per assignment
def main ():
    """Tests at least all of the required functions."""
    # simulates a database
    monthYearTempsDataAvailalable = []

    dataFile = promptTempsDataFileName()
    if dataFile:
        if readTempData(dataFile) is not None:
            monthYear, highTemps, lowTemps = readTempData(dataFile)
            monthYearTempsDataAvailalable.append(monthYear)

            date = input("Enter a date in MMMM DD, YYYY format "
                         "(e.g., March 01, 2022).\n"
                         "Date: ").title()
            validatedDate = dateValidation(date)
            verifiedDate = dataAvailable(validatedDate,
                                         monthYearTempsDataAvailalable,
                                         highTemps)

            if validatedDate is None:
                print(f"{date} is either not a date or does not match "
                      f"designated format (MMMM DD, YYYY).")
            elif verifiedDate is None:
                print(f"No data is available for {date}.")
            else:
                print(f"The daily high for {date}: "
                      f"{dailyHigh(highTemps, verifiedDate)}")
                print(f"The daily low for {date}: "
                      f"{dailyLow(lowTemps, verifiedDate)}")
                print(f"Biggest daily difference in temperature for "
                      f"{verifiedDate[0]} {verifiedDate[2]}: "
                      f"{biggestDailyDifference(highTemps, lowTemps)}")
                print(f"Day(s) of biggest daily difference in temperature "
                      f"for {verifiedDate[0]} {verifiedDate[2]}: ")
                for day in dayOfBiggestDailyDifference(highTemps, lowTemps):
                    print(day)
                print(f"Smallest daily difference in temperature for "
                      f"{verifiedDate[0]} {verifiedDate[2]}: "
                      f"{smallestDailyDifference(highTemps, lowTemps)}")
                print(f"Day(s) of smallest daily difference in temperature "
                      f"for {verifiedDate[0]} {verifiedDate[2]}: ")
                for day in dayOfSmallestDailyDifferece(highTemps, lowTemps):
                    print(day)
                print(f"Average high temperature for "
                      f"{verifiedDate[0]} {verifiedDate[2]}: "
                      f"{monthlyAverage(highTemps):.2f}")
                print(f"Average low temperature for "
                      f"{verifiedDate[0]} {verifiedDate[2]}: "
                      f"{monthlyAverage(lowTemps):.2f}")
                print(f"Days in {verifiedDate[0]} {verifiedDate[2]} "
                      f"with biggest difference in high temperature "
                      f"compared to the next day: ")
                for day in biggestDifferenceBetweenDays(highTemps):
                    print(day)
                print(f"Days in {verifiedDate[0]} {verifiedDate[2]} "
                      f"with biggest difference in low temperature "
                      f"compared to the next day: ")
                for day in biggestDifferenceBetweenDays(lowTemps):
                    print(day)
                print()
                printTemps(monthYear, highTemps, lowTemps)
        else:
            print(f"Data within {dataFile} cannot be parsed.\n"
                  "Verify data is correctly formatted.")
    else:
        print("No temperature data file presented.\n"
              "Exiting program.")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

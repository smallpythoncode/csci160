"""
Jahnke
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Project 01

Simulate a survey asking users for their major. Track the number of
Computer Science, Data Science, and Cyber Security majors. All other
majors are are tracked collectively. Accept inputs for majors until
"done" is input in the prompt.

If the user is a computer science major, prompt him/her for their minor
(if any). Minors to be tracked are Data Science, Cyber Security, and
Mathematics. All other minors and the absences of a minor are tracked
collectively.

After all data is entered, display two tables:
1. The number of students in each tracked major and the collective other
   majors, as well as the percentage for each major.
2. The number of students in each tracked minor and the collective other
   minors/absences of mines, as well as the percentage for each minor.

DEV NOTE - other minors/no minor
The decision was made to separate other minors and no minor for CS
students. This was simple to implement in the program and is more
logical (no_minor != some_minor).

DEV NOTE - Future improvements
One minor improvement on this program could be to have a list of all the
majors offered by UND. This would be beneficial if the scope of the
survey were to track the percentages of all majors. If the user enters a
major that is not in the list, it could prompt the user to correct
his/her input. This, of course, is susceptible to innocent data entry
errors (e.g., entering "history" as "hitsory"), thus, an expansion of
this improvement could be to implement the survey as a GUI (e.g.,
Tkinter) in which the user can select their major from a fixed list.
"""


def welcome_message():
    """Prints a description of the survey and instructions on how to execute.

    :return: None
    """

    print("Greetings!\n"
          "This is a survey of the majors of the students taking CS160.\n"
          "Every student will enter their major when prompted.\n"
          "Computer Science (CS) majors will also be surveyed for their "
          "minor.\n"
          "To complete data entry, enter \"done\" after the major prompt.\n"
          "After completion, the numbers of majors and minors for CS majors "
          "and their percentages will be compiled into a table.\n"
          "\nFORMAT - MAJORS\n"
          "\tCS majors should enter \"cs\"\n"
          "\tData Science majors should enter \"data\"\n"
          "\tCyber Security majors should enter \"cyber\"\n"
          "\tAll other students may enter their major as is or enter "
          "\"other\"\n"
          "\nFORMAT - MINORS\n"
          "\tData Science minors should enter \"data\"\n"
          "\tCyber Security minors should enter \"cyber\"\n"
          "\tMathematics minors should enter \"math\"\n"
          "\tCS students with minor may enter it as is or enter \"other\"\n"
          "\tCS students without a minor may enter \"none\" or simply leave "
          "the line blank and hit \"Enter\"\n"
          )


def prompt_major(tracked_majors=("cs", "data", "cyber"),
                 minors_are_tracked=True,
                 majors_with_minors=None,
                 tracked_minors=("data", "cyber", "math")):
    """Prompts the user to enter their major. Will continue this until
    'done' is entered. For certain majors, the user will be prompted for
    their minor.

    :param tracked_majors: The majors that are to be tracked
    :type tracked_majors: list[str]
    :param minors_are_tracked: If True, minors will be tracked for certain
    majors
    :type minors_are_tracked: bool
    :param majors_with_minors: The majors that have minors to be tracked
    :type majors_with_minors: list[str] or None
    :param tracked_minors: The minors that are tracked with certain majors
    :type tracked_minors: list[str]
    :return: A dictionary with majors as keys with the number of students as
    values. Will return a second similar dictionary for minors if minors
    are tracked.
    :rtype: dict, dict [minors_are_tracked=True] or dict
    [minors_are_tracked=False]
    """

    temp_majors = []
    for major in tracked_majors:
        temp_majors.append(major)
    tracked_majors = {}
    for major in temp_majors:
        tracked_majors[major] = 0
    other_majors = {"other": 0}

    temp_minors = []
    for minor in tracked_minors:
        temp_minors.append(minor)
    tracked_minors = {}
    for minor in temp_minors:
        tracked_minors[minor] = 0
    other_minors = {"other": 0}
    no_minor = {"none": 0}

    if majors_with_minors is None:
        majors_with_minors = ["cs"]

    def prompt_minor():
        """Will update tracked_minors and other_minors (outer scope) if
        certain majors are entered.

        :return: None
        """
        minor_prompt = input("\tEnter a minor: ").lower()
        if minor_prompt in tracked_minors.keys():
            tracked_minors[minor_prompt] += 1
        elif minor_prompt == "" or minor_prompt == "none":
            no_minor["none"] += 1
        else:
            other_minors["other"] += 1

    while True:
        major_prompt = input("Enter a major: ").lower()
        if major_prompt == "done":
            break
        elif major_prompt == "":
            pass
        elif major_prompt in tracked_majors.keys():
            tracked_majors[major_prompt] += 1
            if major_prompt in majors_with_minors and minors_are_tracked:
                prompt_minor()
        else:
            other_majors["other"] += 1

    # ** is unpack_operator
    majors = {**tracked_majors, **other_majors}
    minors = {**tracked_minors, **other_minors, **no_minor}
    if minors_are_tracked:
        return majors, minors
    else:
        return majors


def majors_table(major_data, course="CSCI 160", major_legend=None):
    """Prints a formatted table of majors, the number of students with that
    major, and the percentage of students with that major.

    :param major_data: The majors of the students who've taken the survey and
    the number of those students
    :type major_data: dict
    :param course: The title of the course to be surveyed
    :type course: str
    :param major_legend: The translation of data entered as the key with what
    appears in the table as the value
    :type major_legend: dict
    :return: None
    """

    if major_legend is None:
        major_legend = {"cs": "Computer Science",
                        "data": "Data Science",
                        "cyber": "Cyber Security",
                        "other": "Other Majors"}
    total_students = sum(major_data.values())
    print(f"Total number of students: {total_students}\n")

    print("Majors of Students in", course)
    if total_students == 0:
        print("NO DATA ENTERED")
    else:
        print(format("MAJOR", "20s"), format("NUM", "3s"), format("PERCENT",
                                                                  "7s"))
        for key, value in major_data.items():
            if key in major_legend.keys():
                print(f"{major_legend[key]:20s}", f"{value:>3d}",
                      f"{value / total_students * 100:>7.2f}")
            else:
                print(f"{key:20s}", f"{value:>3d}",
                      f"{value / total_students * 100:>7.2f}")


def minors_table(minor_data, course="CSCI 160", minor_legend=None,
                 majors_with_minors=None):
    """Prints a formatted table of minors, the number of students with that
    minor, and the percentage of students with that minor.

    :param minor_data: The minors of the students who've taken the survey and
    the number of those students
    :type minor_data: dict
    :param course: The title of the course to be surveyed
    :type course: str
    :param minor_legend: The translation of data entered as the key with what
    appears in the table as the value
    :type minor_legend: dict
    :param majors_with_minors: The majors that have minors to be tracked;
    depicted in the table title
    :type majors_with_minors: list[str]
    :return: None
    """

    if minor_legend is None:
        minor_legend = {"data": "Data Science",
                        "cyber": "Cyber Security",
                        "math": "Mathematics",
                        "other": "Other Minors",
                        "none": "No Minor"}
    if majors_with_minors is None:
        majors_with_minors = ["Computer Science"]
    total_minor_responses = sum(minor_data.values())

    if len(majors_with_minors) == 1:
        print(f"Minors of {majors_with_minors[0]} Students in", course)
    elif len(majors_with_minors) == 2:
        print(f"Minors of {majors_with_minors[0]} and "
              f"{majors_with_minors[1]} Students in", course)
    else:
        print("Minors of ",
              ', '.join(f"{minor}" for minor in majors_with_minors[:-1]), ", ",
              f"and {majors_with_minors[-1]} Students in ", course, sep="")

    print(format("MINOR", "20s"), format("NUM", "3s"), format("PERCENT", "7s"))
    for key, value in minor_data.items():
        if key in minor_legend.keys():
            print(f"{minor_legend[key]:20s}", f"{value:>3d}",
                  f"{value / total_minor_responses * 100:>7.2f}")
        else:
            print(f"{key:20s}", f"{value:>3d}",
                  f"{value / total_minor_responses * 100:>7.2f}")


if __name__ == "__main__":
    welcome_message()
    project_majors, project_minors = prompt_major()
    print()
    if sum(project_majors.values()) > 0:
        majors_table(project_majors)
        print()
        if project_majors["cs"] > 0 and project_minors:
            minors_table(project_minors)
        else:
            print("No Computer Science majors took this survey; no minor data "
                  "to report.")
    else:
        print("No data was entered in this survey.")

# All work and no play makes Jack a dull boy.

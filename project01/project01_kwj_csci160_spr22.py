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

DEV NOTE
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
    print("Greetings!\n"
          "This is a survey of the majors of the students taking CS160.\n"
          "Have every student enter their major when prompted.\n"
          "Computer Science majors will also be surveyed for their minor.\n"
          "To complete data entry, enter \"done\" after the major prompt.\n"
          "After completion, the numbers of majors and minors for CS majors "
          "and their percentages will be compiled into a table.\n"
          "\nFORMAT - MAJORS\n"
          "\tComputer Science (CS) majors should enter \"cs\"\n"
          "\tData Science majors should enter \"data\"\n"
          "\tCyber Security majors should enter \"cyber\"\n"
          "\tAll other students may enter their major as is or enter "
          "\"other\"\n"
          "\nFORMAT - MINORS\n"
          "\tData Science minors should enter \"data\"\n"
          "\tCyber Security minors should enter \"cyber\"\n"
          "\tMathematics minors should enter \"math\"\n"
          "\tAll other CS students may enter their minor as is or enter "
          "\"other\"\n"
          "\tCS students without a minor may enter \"none\" or simply leave "
          "leave the line blank and hit \"Enter\"\n"
          )

# FIXME: reassign tracked majors as a default list, exclude None
# FIXME: may need to be a tuple, can a list be passed in??
# avoiding mutable argument https://docs.python-guide.org/writing/gotchas/
def prompt_major(tracked_majors=None, minors_are_tracked=True,
                 majors_with_minors=None, tracked_minors=None):
    # establishes default tracked_majors
    if tracked_majors is None:
        tracked_majors = {"cs": 0, "data": 0, "cyber": 0}
    else:
        temp_majors = []
        for major in tracked_majors:
            temp_majors.append(major)
        tracked_majors = {}
        for major in temp_majors:
            tracked_majors[major] = 0

    other_majors = {"other": 0}

    # establishes default tracked minors with specific  majors
    if minors_are_tracked and majors_with_minors is None and \
            tracked_minors is None:
        tracked_minors = {"data": 0, "cyber": 0, "math": 0}
        majors_with_minors = ["cs"]
    other_minors = {"other/none": 0}

    def prompt_minor():
        minor_prompt = input("Enter a minor: ").lower()
        if minor_prompt in tracked_minors.keys():
            tracked_minors[minor_prompt] += 1
        else:
            other_minors["other/none"] += 1

    while True:
        major_prompt = input("Enter a major: ").lower()
        if major_prompt == "done":
            break
        elif major_prompt == "":
            pass
        elif major_prompt in tracked_majors.keys():
            tracked_majors[major_prompt] += 1
            if major_prompt in majors_with_minors:
                prompt_minor()
        else:
            other_majors["other"] += 1

    # unpack operator
    majors = {**tracked_majors, **other_majors}
    minors = {**tracked_minors, **other_minors}
    return majors


if __name__ == "__main__":
    welcome_message()
    these_majors = ["yolo", "bumpy"]
    print(prompt_major(these_majors))
    # print(prompt_major())




# major_tallies = {"Computer Science": 0, "Data Science": 0}
#
# major_tallies["Computer Science"] += 1
#
# print(major_tallies)

# All work and no play makes Jack a dull boy.

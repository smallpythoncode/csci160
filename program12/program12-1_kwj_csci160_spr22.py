"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Program 12, Part 1
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    # TODO

.. note::
    Function HEADERS are written exactly as specified per assignment
    instructions, i.e., written in camelCase with whitespace between the
    function's name and its parameters. camelCase persists for
    declaration of variables for consistency. When a function is called,
    the absence of whitespace between a function's name and its
    arguments was judged to have no effect on performance; thus, such
    whitespace is excluded outside of function headers.

Functions:
    promptTextFileWrite ()
        - Prompts for desired text file name for use in write mode.

"""

from os.path import isfile


def promptTextFileWrite ():
    """Prompts for desired text file name for use in write mode.

    Designed to use in conjunction with writing of files, thus, checks
    if text file of same name already exists to circumvent undesired
    overwriting.

    :return:
        Name of text file to be (over)written
    :rtype: str
    """
    while True:
        fileName = input("Text file name: ").lower()
        if fileName[-4:] != ".txt":
            print("File name must include \".txt\" extension.")
        elif not isfile(fileName):
            return fileName
        else:
            print(fileName, "already exists. Do wish to overwrite?")
            while True:
                overwritePrompt = input("y/n: ").lower()
                if overwritePrompt in ["y", "yes"]:
                    return fileName
                elif overwritePrompt in ["n", "no"]:
                    break


# TODO
def writeDictToFile (theDictionary, fileName, delimiter="\t"):
    """Writes the contents of a theDictionary to fileName.

    Writes one key/value pair per line within the file in format
    "KEY[delimiter]VALUE".

    Designed primarily for use with text files. Writing to other file
    types may have unintended consequences.

    :param dict theDictionary:
        The dict to write to fileName
    :param str fileName:
        The name of the file to write to
    :param str delimiter:
        The character by which to delimit keys from values when writing
        a line of data to fileName
    :rtype: None
    """
    with open(fileName, "w") as f:
        for key in theDictionary:
            f.write (f"{key}{delimiter}{theDictionary[key]}\n")


def main():
    diction = {"first": None, "second": 1}
    file = "bumpy.txt"
    writeDictToFile(diction, file)



if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

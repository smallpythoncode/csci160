"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Lab 10
Copyright (C) 2022 Kenneth Jahnke

"""

from os.path import isfile


def generate_example():
    """Generates an example of a text file for language data.

    :return:
    """
    example = {
        'one': 'uno',
        'two': 'dos',
        'three': 'tres',
        'four': 'cuatro',
        'five': 'cinco',
        'six': 'seis',
        'seven': 'sieto',
        'eight': 'ocho',
        'nine': 'nueve',
        'ten': 'diez'
    }

    file = "example_dictionary.txt"
    with open(file, "w") as f:
        for i in example:
            f.write(f"{i}:{example[i]}\n")


def txt_to_dict(file=None):
    """Converts text file language data to a dictionary.

    Designed for English to Spanish translation. Use this as a
    guideline when developing text files for other languages.

    :param str file:
        The name of the text file from which to convert translation
        data to a dict. If no argument is presented, defaults to
        "example_dictionary.txt". Format of line data:
        "ENGLISHWORD:SPANISHWORD"
    :return:
        If file is a text file and its data is formatted correctly,
        will return the dict with English words as keys and
        corresponding Spanish word as values. Otherwise, returns None.
    :rtype: dict[str, Union[int, None, dict[int, str]]
    """
    return_data = {
        "code": 0,
        "data": None,
        "legend": {
            1: "Data from text file parsed into dictionary.",
            0: "No data.",
            -1: "File does not exist.",
            -2: "No text file detected. Data must be in text file to parse.",
            -3: "Data formatting incorrect. Check data."
        }
    }



    if file is None:
        file = "example_dictionary.txt"
        if not isfile(file):
            generate_example()

    if not isfile(file):
        return_data["code"] = -1
    if file[-4:] != ".txt":
        return_data["code"] = -2
    else:
        dictionary = {}
        with open(file) as f:
            for line in f:
                translation = line.split(":")
                for i in range(len(translation)):
                    translation[i] = translation[i].strip()
                if (
                    len(translation) != 2 or
                    not translation[0].isalpha() or
                    not translation[1].isalpha()
                ):
                    return_data["code"] = -3
                else:
                    dictionary[translation[0]] = translation[1]

        return dictionary





def main():
    print(txt_to_dict())


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

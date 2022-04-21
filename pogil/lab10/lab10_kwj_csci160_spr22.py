"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / greensaber77@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Lab 10
Copyright (C) 2022 Kenneth Jahnke

# TODO description

Functions:

    generate_example():
        - Generates an example language data file in working directory.
    txt_to_dict(file=None, metadata=False):
        - Converts language translation data from file to a dict.


"""

from os.path import isfile


def generate_example():
    """Generates an example language data file in working directory.

    :rtype: None
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


def txt_to_dict(file=None, metadata=False):
    """Converts language translation data from file to a dict.

    Designed for English to Spanish translation. Use this as a
    guideline when developing text files for other languages.

    Accounts for words with apostrophes.

    :param str file:
        The name of the text file from which to parse translation
        data to a dict. If no argument is presented, defaults to
        "example_dictionary.txt". Format of line data:
        "ENGLISHWORD:SPANISHWORD"
    :param bool metadata:
        Determines whether just the data or data and its metadata is
        returned
    :return:
        If metadata=True, a dict containing information as to why
        None would be returned if metadata=False: the data or None
        (indicating file doesn't exist or data is formatted
        incorrectly), a status code, and a legend for the status
        codes.
        If metadata=False, a dict with English words as the keys and
        Spanish words as the respective values.

        fdsa
    :rtype: dict[str, Union[int, None, dict[int, str]]
    """
    return_data = {
        "data": None,
        "code": 0,
        "legend": {
            1: "Translation data acquired.",
            0: "No data.",
            -1: "File does not exist.",
            -2: "Data formatting incorrect. Check data."
        }
    }

    # None assigned as default argument instead of example_dictionary.txt to
    # allow for generation of example if not present
    if file is None:
        file = "example_dictionary.txt"
        if not isfile(file):
            generate_example()

    if not isfile(file):
        return_data["code"] = -1
    else:
        dictionary = {}
        with open(file) as f:
            for line in f:
                translation = line.split(":")
                # remove new line character
                for i in range(len(translation)):
                    translation[i] = translation[i].strip()
                english_apostrophe = translation[0].replace("'", "")
                spanish_apostrophe = translation[1].replace("'", "")
                if (
                    len(translation) != 2 or
                    not english_apostrophe.isalpha() or
                    not spanish_apostrophe.isalpha()
                ):
                    return_data["code"] = -2
                    break
                else:
                    dictionary[translation[0]] = translation[1]
                    # return_data["code"] will remain 0 if file is empty
                    return_data["code"] = 1
        if return_data["code"] == 1:
            return_data["data"] = dictionary

    if metadata:
        return return_data
    else:
        return return_data["data"]


def english_to_spanish(dictionary, word):
    """
    # TODO
    :param dictionary:
    :param word:
    :return:
    """
    for key in dictionary:
        if key == word:
            return dictionary[key]


def spanish_to_english(dictionary, word):
    """
    # TODO
    :param dictionary:
    :param word:
    :return:
    """
    # spanish = dictionary.values()
    # english = dictionary.keys()

    for i in range(len(list(dictionary.values()))):
        if list(dictionary.values())[i] == word:
            return list(dictionary.keys())[i]


def main():
    translation = txt_to_dict()
    print(txt_to_dict())
    print(translation.values())

    print(english_to_spanish(translation, "oneghfdgdfs"))
    print(spanish_to_english(translation, "uno"))

    # TODO write for loop that ends with blank



if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

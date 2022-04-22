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
    english_to_spanish(dictionary, word):
        - Returns the translation of an English word (if in dictionary).


"""

from os.path import isfile


def generate_example():
    """Generates an example language data file in working directory.

    :rtype:
        None
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
    :rtype:
        dict
    """
    return_data = {
        "data": None,
        "code": 0,
        "legend": {
            1: "Translation data acquired.",
            0: "No data.",
            -1: "File does not exist.",
            -2: "Data formatting incorrect."
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
    """Translates an English word to Spanish.

    Current version this function is incapable of parsing translation
    data within a metadata dict (see txt_to_dict documentation).

    :param dict[str, str] dictionary:
        Keys are an English word and the value is the respective Spanish
        translation. Use this guideline when expanding an
        English/Spanish dictionary or developing dictionaries for other
        languages.
    :param str word:
        The English word to be translated
    :return:
        The Spanish translation of word if within dictionary, else None.
    :rtype:
        str or None
    """
    for key in dictionary:
        if key == word:
            return dictionary[key]

# TODO
def spanish_to_english(dictionary, word):
    """Translates a Spanish word to English.

    Current version this function is incapable of parsing translation
    data within a metadata dict (see txt_to_dict documentation).

    :param dict[str, str] dictionary:
        Keys are an English word and the value is the respective Spanish
        translation. Use this guideline when expanding an
        English/Spanish dictionary or developing dictionaries for other
        languages.
    :param str word:
        The Spanish word to be translated
    :return:
        The English translation of word if within dictionary, else None.
    :rtype:
        str or None
    """
    for i in range(len(list(dictionary.values()))):
        if list(dictionary.values())[i] == word:
            return list(dictionary.keys())[i]


def main():
    print("Welcome")

    while True:
        file = input("Enter name of language translation data file: ")
        dictionary = txt_to_dict(file)

        # not None, i.e., translation data acquired
        if dictionary is not None:
            print("Enter an English word to find its Spanish translation.\n"
                  "To quit, press \"Enter\".")
            # TODO
            while True:
                word = input("Word to translate: ").lower()
                if word == "":
                    break
                elif english_to_spanish(dictionary, word) is not None:
                    print(f"The Spanish translation is "
                          f"{english_to_spanish(dictionary, word)}.")
                elif spanish_to_english(dictionary, word) is not None:
                    print(f"That is a Spanish word.\nIt's English translation "
                          f"is {spanish_to_english(dictionary, word)}.")
                else:
                    print(f"There is no available tranlsation for the word "
                          f"{word}.")
            break

        else:
            print(f"{file} either does not exist or its data is improperly "
                  f"formatted.Options:\n\t"
                  f"- Enter custom file name again.\n\t"
                  f"- Enter \"example_dictionary.txt \n\t"
                  f"- press \"Enter\" to exit.")





if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

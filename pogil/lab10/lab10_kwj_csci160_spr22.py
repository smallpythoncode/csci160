"""Jahnke, Student ID: 0808831
kenny.jahnke@ndus.edu / smallpythoncode@gmail.com
CSCI 160, Spring 2022, Lecture Sect 02, Lab Sect L03
Lab 10
Copyright (C) 2022 Kenneth Jahnke

Assignment:
    1. Prompt user for text file containing translation data.
        - Designed for English/Spanish translation
        - Could be any language pair
        - Line format: "ENGLISHWORD:SPANISHWORD"
    2. Prompt user for word to translate.
        - If word is English, will output Spanish translation
        - If word is Spanish, will output English translation
        - Notifies user if translation is not available for desired word
        - Continues to prompt until user presses "Enter" (blank)

Functions:
    generate_example():
        - Generates an example language data file in working directory.
    txt_to_dict(file=None, metadata=False):
        - Converts language translation data from file to a dict.
    english_to_spanish(dictionary, word):
        - Translates an English word to Spanish.
    spanish_to_english(dictionary, word):
        - Translates a Spanish word to English.


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
    print("Welcome. In this program we will translate English words to "
          "Spanish.")

    # future version could incorporate a flag within input to indicate that
    # text_to_dict would return metadata dictionary
    # see english_to_spanish and spanish_to_english documentation for context
    while True:
        file = input("Enter name of language translation data file: ")
        if file == "exit":
            break
        elif file == "":
            # utilize "example_dictionary.txt"
            dictionary = txt_to_dict()
        else:
            dictionary = txt_to_dict(file)

        # not None, i.e., translation data acquired
        if dictionary is not None:
            print("Enter an English word to find its Spanish translation.\n"
                  "To quit, press \"Enter\".")

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
                    print(f"There is no available translation for the word "
                          f"{word}.")
            break

        else:
            print(f"{file} either does not exist or its data is improperly "
                  f"formatted.\nEnter name of valid dictionary file name "
                  f"or enter \"exit\".")


if __name__ == "__main__":
    main()

# All work and no play makes Jack a dull boy.

#!/usr/bin/python3
""" 5-text_indentation Module """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    text: a string

    Raises:
    TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")), end="")

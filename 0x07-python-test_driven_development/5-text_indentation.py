#!/usr/bin/python3

"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text="souad"):

    """
    arge:
    -----
    txt : string argement

    Raises:
    -------
    raise TypeError in text not a string
    """

    # text's check
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # test funtion
    c = 0
    while c < len(text):
        if text[c] == '.' or text[c] == ':' or text[c] == '?':
            print(text[c])
            c += 1
            c += 1
        else:
            print(text[c], end="")
            c += 1

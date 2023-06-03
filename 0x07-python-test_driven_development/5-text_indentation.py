#!/usr/bin/python3

"""This module contains a function ``text_indentation`` that prints a text with two new lines after each of these characters: '.', '?' and ':'
"""
def text_indentation(text):
    """This function prints out a text with 2 new lines after characters: '.', '?' and ':'
    args:
        text: a string of characters
    raise:
        TypeError: text must be a string
    return:
        void
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    newString = ""
    for i in range(len(text)):
        if i == 0:
            newString += text[i]
        elif i > 0 and (text[i - 1] not in ['.', '?', ':']):
            newString += text[i]

        if text[i] in ['.', '?', ':']:
            newString += "\n\n"
    print(newString)

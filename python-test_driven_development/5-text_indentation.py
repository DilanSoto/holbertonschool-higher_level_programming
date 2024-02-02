#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after each characters: ., ? and :
    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    Returns:
        None: The text is printed.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join([line.strip() for line in text.split("\n")]), end="")

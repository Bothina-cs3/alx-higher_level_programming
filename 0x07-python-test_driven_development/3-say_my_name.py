#!/usr/bin/python3
"""Defines a function that prints My name

Attributes:
    say_my_name: function that prints My name.
"""


def say_my_name(first_name, last_name=""):
    """prints My name.

    Args:
        first_name (str): My first name.
        last_name (str, optional) My second name. Defaults to"".

    Raises:
         TypeError: If either first name or last name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

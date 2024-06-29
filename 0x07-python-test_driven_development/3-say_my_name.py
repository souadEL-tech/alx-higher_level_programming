#!/usr/bin/python3

"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):

    """
    this function prints My name is <first name> <last name>
    args:
    ------
    first_name : string
    last_name : string

    Raises:
    -------
     TypeError: If either of first_name or last_name are not strings.
    """
    # check if first and last name are string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

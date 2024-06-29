#!/usr/bin/python3

def say_my_name(first_name, last_name=""):

    """
    this function prints My name is <first name> <last name>
    args:
    ------
    first_name : string
    last_name : string

    Return:
    -------
    print  My name is <first name> <last name>
    """
    # check if first and last name are string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))

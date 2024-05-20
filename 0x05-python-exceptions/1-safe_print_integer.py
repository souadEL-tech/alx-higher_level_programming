#!/usr/bin/python3

def safe_print_integer(value):
    # check if val is an integer
    try:
        if value == int(value):
            print("{:d}".format(value))
    except Exception:
        return (False)
    else:
        return (True)

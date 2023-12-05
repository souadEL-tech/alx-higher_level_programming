#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    curs = len(my_list) - 1

    while curs <= 0:
        print(my_list[curs])
        curs -= 1

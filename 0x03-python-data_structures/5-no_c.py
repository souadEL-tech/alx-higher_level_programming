#!/usr/bin/python3

def no_c(my_string):

    j = 0
    my_str = ""

    for i in range(len(my_string)):
        if my_string[i] != 'c' or my_string[i] != 'C':
            my_str[j] = my_string[i]
            j += j
    return my_str

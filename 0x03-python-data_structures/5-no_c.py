#!/usr/bin/python3

def no_c(my_string):

    j = 0
    my_str = ""

    for i in range(len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass
        else:
            my_str[j] = my_string[i]
            j += 1
    return (my_str)

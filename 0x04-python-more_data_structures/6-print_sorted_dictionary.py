#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    list_keys = list(a_dictionary.keys())

    for i in range(len(list_keys)):
        j = i + 1
        for j in range(len(list_keys)):
            if list_keys[i] < list_keys[j]:
                tmp = list_keys[i]
                list_keys[i] = list_keys[j]
                list_keys[j] = tmp
    for m in list_keys:
        print("{}: {}".format(m, a_dictionary[m]))

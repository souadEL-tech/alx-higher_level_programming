#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    # new list of keys
    keys_list = list(a_dictionary.keys())

    # check if the key exist
    for i in range(len(keys_list)):
        if keys_list[i] == key:
            a_dictionary[keys_list[i]] = value
        else:
            a_dictionary[key] = value
    return (a_dictionary)

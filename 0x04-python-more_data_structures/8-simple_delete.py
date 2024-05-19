#!/usr/bin/python3

# delete key

def simple_delete(a_dictionary, key=""):

    # search for the key
    list_key = list(a_dictionary.keys())

    for i in range(len(list_key)):
        if list_key[i] == key:
            del a_dictionary[list_key[i]]
        else:
            pass
    return (a_dictionary)

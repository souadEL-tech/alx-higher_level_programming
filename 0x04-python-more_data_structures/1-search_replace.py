#!/usr/bin/python3
def search_replace(my_list, search, replace):

    new_list = []
    len_list = len(my_list)

    for i in range(len_list):
        if search == my_list[i]:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return (new_list)

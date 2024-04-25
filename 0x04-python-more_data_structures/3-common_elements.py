#!/usr/bin/python3

def common_elements(set_1, set_2):

    # Intersection
    my_set = set()
    for i in set_1:
        if i in set_2:
            my_set.add(i)
        else:
            pass
    return (my_set)

#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    # difference methode
    deff_set = set()
    for i in set_1:
        if i not in set_2:
            deff_set.add(i)
        else:
            pass
    for j in set_2:
        if j not in set_1:
            deff_set.add(j)
        else:
            pass

    return (deff_set)

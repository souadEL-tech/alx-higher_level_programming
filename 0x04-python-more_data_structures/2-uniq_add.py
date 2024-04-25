#!/usr/bin/python3

def uniq_add(my_list=[]):

    uni_list = list()
    result = 0
    
    uni_list.append(my_list[0])
    for i in my_list:
        if i not in uni_list:
            uni_list.append(i)
        else:
            pass
    for j in uni_list:
        result = result +j
    return result

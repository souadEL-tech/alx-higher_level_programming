#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    list_len = len(my_list)
    Result = 0

    new_list.append(my_list[0])
    for i in range(1, list_len):
        print("this is i {:d}".format(i))
        for j in new_list:
            print("this is the j : {:d}".format(j))
            if my_list[i] != j:
                new_list.append(my_list[i])
            else:
                pass
    for some in new_list:
        print("{:d}".format(some))
        # Result = some + Result
    return (Result)

#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    Item_num = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            Item_num += 1

    except Exception as e:
        pass

    print("")
    return (Item_num)

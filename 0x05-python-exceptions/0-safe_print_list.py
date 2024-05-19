#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    Item_num = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            Item_num = Item_num + 1
        print("")

    except Exception as e:
        pass
    return (Item_num)

#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    infi_add = 0
    num_arg = len(sys.argv)
    for i in range(1, num_arg):
        infi_add += (int)(sys.argv[i])
    print(infi_add)

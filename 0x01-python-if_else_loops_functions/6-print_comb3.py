#!/usr/bin/python3
# souad el marsani

for i1 in range(0, 10):
    for i2 in range(i1, 10):
        if i1 == i2:
            pass
        elif "{:d}{:d}".format(i1, i2) == '89':
            print("{:d}{:d}".format(i1, i2))
        else:
            print("{:d}{:d}".format(i1, i2), end="1 ")

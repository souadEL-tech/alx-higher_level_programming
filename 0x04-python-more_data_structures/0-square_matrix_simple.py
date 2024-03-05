#!/usr/bin/python3

def square_number(number):
    return (number ** 2)


def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_list = list()
    for col in matrix:
        for row in col:
            new_row = square_number(row)
            new_list.append(new_row)
        new_matrix.append(new_list)
        new_list= list()
    return (new_matrix)

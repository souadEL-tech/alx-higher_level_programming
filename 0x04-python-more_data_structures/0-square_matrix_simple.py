#!/usr/bin/python3

def square_number(number):
    return (number ** 2)


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        for row in col:
            new_row = square_number(row)
            new_matrix.append(new_row)
    return (new_matrix)

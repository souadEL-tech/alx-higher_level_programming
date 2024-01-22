#!/usr/bin/python3

def square_map(number):
    return (number ** 2)


def square_matrix_simple(matrix=[]):

    # declare new matrix
    new_matrix = []

    # parcour the old one
    for i in matrix:
        result = list(map(square_map, i))
        new_matrix.append(result)
    return (new_matrix)

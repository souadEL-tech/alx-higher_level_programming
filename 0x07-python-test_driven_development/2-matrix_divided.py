#!/usr/bin/python3

def matrix_divided(matrix, div):

    """
    matrix_divided: a function that divides all elements of a matrix.
    --------------

    args:
    -----
    *matricx : list of lists
    *divided : number int / float

    Return
    ------
    return new matrix

    """
    new_matrix = list()

    # check: div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # check : length of matrix
    m_len = len(matrix[0])
    for i in matrix:
        if len(i) == m_len:
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
    # check : all element are integres or floats
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                pass
    

    # divide all element
    for ligne in matrix:
        new_list = list()
        for column in ligne:
            result = round((column / div), 2)
            new_list.append(result)
        new_matrix.append(new_list)

    # RETURN
    return (new_matrix)

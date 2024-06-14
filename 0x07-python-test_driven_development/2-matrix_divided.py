#!usr/bin/python3

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
    # message of TypeError
    message = "matrix must be a matrix (list of lists)of integers/floats"
    new_matrix = list()


    # check matrix item:
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(message)

    # chech the size of lists
    length = len(matrix[0])
    for leng in matrix:
        if len(leng) != length:
            raise TypeError("Each row of the matrix must have the same size")

    # check div type
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    # division

    for line in range(len(matrix)):
        new_list = list()
        for col in range(len(matrix[line])):
            result = round((matrix[line][col] / div), 2)
            new_list.append(result)
        new_matrix.append(new_list)

    #return
    return (new_matrix)

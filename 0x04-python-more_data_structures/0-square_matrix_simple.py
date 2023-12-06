#!/usr/bin/python3

def square_matrix_simple(matrix=None):
    if matrix is None:
        matrix = []

    firstL = len(matrix)
    finalA = []

    for i in range(firstL):
        secondL = len(matrix[i])
        miniA = []
        finalA.append(miniA)

        for j in range(secondL):
            miniA.append(matrix[i][j] ** 2)

    return finalA

from typing import T


def rotate_matrix(matrix):
    """
    Function for rotating square matrix's.

    """
    assert len(matrix) == len(matrix[0]), "Matrix must be square"

    n = len(matrix)

    for layer in range(n // 2):
        for i in range(layer, n - layer - 1):
            top = matrix[layer][i]
            right = matrix[i][n - layer - 1]
            bottom = matrix[n - layer - 1][n - i - 1]
            left = matrix[n - i - 1][layer]

            matrix[layer][i] = left
            matrix[i][n - layer - 1] = top
            matrix[n - layer - 1][n - i - 1] = right
            matrix[n - i - 1][layer] = bottom


    return matrix

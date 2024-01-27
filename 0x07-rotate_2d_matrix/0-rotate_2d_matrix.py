#!/usr/bin/python3
"""
Rotates a matrix by 90 degrees clockwise
Args: matrix (List[List[int]]): The input 2D matrix.

Returns: None. The matrix is edited in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List[int]]): The input 2D matrix.

    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]


if __name__ == "__main__":
    """
    Test the rotate_2d_matrix function with different matrices.
    """

    # Test Case 1
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    rotate_2d_matrix(matrix1)
    print("Rotated Matrix:")
    for row in matrix1:
        print(row)

    # Test Case 2
    matrix2 = [[1, 11, 13, 19],
               [41, 32, 6, 22],
               [55, 21, 41, 66],
               [77, 29, 78, 2]]
    rotate_2d_matrix(matrix2)
    print("Rotated Matrix:")
    for row in matrix2:
        print(row)

    # Test Case 3
    matrix3 = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
    rotate_2d_matrix(matrix3)
    print("Rotated Matrix:")
    for row in matrix3:
        print(row)

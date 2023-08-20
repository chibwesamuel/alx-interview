#!/usr/bin/python3
"""
Rotates a matrix by 90 degrees clockwise
Args: matrix (List[List[int]]): The input 2D matrix.

Returns: None. The matrix is edited in-place.
"""


def rotate_2d_matrix(matrix: List[List[int]]) -> None:
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
    """ Test the rotate_2d_matrix function"""
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    rotate_2d_matrix(matrix)
    
    print("Rotated Matrix:")
    for row in matrix:
        print(row)

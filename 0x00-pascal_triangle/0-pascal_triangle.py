#!/usr/bin/python3
# Samuel Mukosa Chibwe
"""
Returns a list of lists of integers representing Pascal’s triangle of n.
Returns an empty list if n <= 0.
You can assume n will always be an integer.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of size n.

    Parameters:
    - n: An integer representing the size of the Pascal's triangle.

    Returns:
    - A list of lists representing Pascal's triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row [1]
    
    for i in range(1, n):
        row = [1]  # Start each row with 1
        
        # Calculate the values for the current row based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the row to the triangle

    return triangle


def print_triangle(triangle):
    """
    Prints the Pascal's triangle.

    Parameters:
    - triangle: A list of lists representing Pascal's triangle.
    """

    for row in triangle:
        # Convert each integer in the row to a string and join them with commas
        row_str = ",".join([str(x) for x in row])
        print("[{}]".format(row_str))


if __name__ == "__main__":
    triangle = pascal_triangle(5)  # Generate Pascal's triangle of size 5
    print_triangle(triangle)  # Print the generated triangle


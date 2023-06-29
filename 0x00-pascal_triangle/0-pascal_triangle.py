#!/usr/bin/python3
# Samuel Mukosa Chibwe
"""
Returns a list of lists of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer
"""


def pascal_triangle(n):
	"""Definition of the pascal tiangle"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle


def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))


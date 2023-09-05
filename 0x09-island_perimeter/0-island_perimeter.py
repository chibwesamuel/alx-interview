#!/usr/bin/python3
"""
This script defines a function to calculate the perimeter of an island
described in a 2D grid. The grid is represented as a list of lists of
integers, where 1s represent land and 0s represent water. The function
iterates through the grid, calculating the perimeter of the land by
considering neighboring cells. The final perimeter value is returned.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in a grid.

    Args:
        grid (list[list[int]]): A list of lists of integers representing
        the island grid.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

---

# Island Perimeter

## Description

The **Island Perimeter** is a Python function that calculates the perimeter of an island described in a given grid. The grid is represented as a list of lists of integers, where each integer value has a specific meaning:
- `0`: Represents water
- `1`: Represents land
Each cell in the grid is a square with a side length of 1 unit, and cells are connected only horizontally or vertically (not diagonally). The grid is also guaranteed to be rectangular, with its width and height not exceeding 100 units. The grid is completely surrounded by water.

## Function Signature

```python
def island_perimeter(grid: List[List[int]]) -> int:
    pass
```

## Input

- `grid`: A list of lists of integers representing the island grid.

## Output

- Returns an integer representing the perimeter of the island.

## Usage

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
perimeter = island_perimeter(grid)
print(perimeter)  # Output: 12
```

## Constraints

- The grid is completely surrounded by water.
- There is only one island (or nothing).
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

## Implementation

The function iterates through each cell in the grid and checks if it's land (`1`). If it's land, it counts how many sides of the cell are adjacent to water (`0`). The sum of the adjacent water sides for all land cells gives the perimeter of the island.

---

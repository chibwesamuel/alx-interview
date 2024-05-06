# Island Perimeter

This project contains a Python function named `island_perimeter` which calculates the perimeter of an island described in a given grid.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.4.3
- Files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- Code should follow PEP 8 style (version 1.7)
- No module imports allowed
- All modules and functions must be documented

## Task

### 0. Island Perimeter
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:

- `grid` is a list of list of integers:
    - 0 represents water
    - 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally).
- `grid` is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

## Usage

```bash
./0-main.py
```

Sample Output:
```
12
```

## Author
Samuel Mukosa Chibwe - [Github](https://github.com/chibwesamuel)

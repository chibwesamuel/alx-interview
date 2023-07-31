# N Queens
### N Queens Solver - Python Implementation

## Introduction

Welcome to the N Queens Solver project! In this project, I demonstrate a Python implementation of the N queens puzzle, a classic chess problem. The challenge is to place N non-attacking queens on an N×N chessboard. This program will find and print all possible solutions to the N queens problem, given a specific integer N.

## Requirements

### General

- **Editor used:** vi
- **Interpreted/Compiled On:** Ubuntu 14.04 LTS using Python3 (version 3.4.3)
- **Shebang Line:** `#!/usr/bin/python3`
- **Coding Style:** PEP 8 style (version 1.7.*)

### Task

#### Task 0: N queens (mandatory)

The N queens puzzle is about placing N non-attacking queens on an N×N chessboard. Your task is to write a program that solves this N queens problem.

**Usage:**
```
nqueens N
```

**Constraints:**
- N must be an integer greater or equal to 4
- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status 1
- If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status 1

**Output:**
- The program should print every possible solution to the problem.
- One solution per line.
- The format of the solution should follow the example provided below.
- The order of solutions does not need to be specific.

**Example:**

```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

**Note:**
- You are only allowed to import the `sys` module.

## Repository Information

- **GitHub Repository:** [alx-interview](https://github.com/chibwesamuel/alx-interview)
- **Directory:** 0x05-nqueens
- **File:** 0-nqueens.py

## Conclusion

Thank you for checking out the N Queens Solver project! If you have any questions or feedback, please feel free to reach out to me. Happy coding!

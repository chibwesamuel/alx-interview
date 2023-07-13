# Minimum Operations

This is a coding project that aims to calculate the fewest number of operations required to obtain a specific number of characters in a text file.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, located at the root of the project folder, is mandatory
- Code should be documented
- Code should follow the PEP 8 style (version 1.7.x)
- All files must be executable

## Task

### Minimum Operations

In a text file, there is a single character 'H'. The text editor allows two operations: Copy All and Paste. Given a number `n`, the task is to write a method that calculates the fewest number of operations needed to have exactly `n` 'H' characters in the file.

- Prototype: `def minOperations(n)`
- Returns an integer
- If `n` is impossible to achieve, return 0

Example:

```
n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
```

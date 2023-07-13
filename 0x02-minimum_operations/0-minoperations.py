#!/usr/bin/python3
"""
Executes Copy All and Paste file operations
Returns an integer
If n is impossible to achieve, return 0
"""

def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to obtain n 'H' characters.
    """
    if n <= 1:
        return 0

    operations = 0
    copy = 1
    total = 1

    while total < n:
        if n % total == 0:
            copy = total
            operations += 1
        total += copy
        operations += 1

    return operations

if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


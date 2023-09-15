#!/usr/bin/python3
"""
Prime Game Solver

This script contains a function to determine the winner of the Prime Game
based on a given number of rounds and the maximum value for each round.

The Prime Game is a two-player game where Maria and Ben take turns choosing
a prime number from a set of consecutive integers starting from 1 up to and
including n. They remove the chosen number and its multiples from the set.
The player who cannot make a move loses the game. The function calculates
the winner of the game based on the number of prime numbers available and
the total number of rounds played.

Author: Samuel Mukosa Chibwe
"""


def is_prime(n):
    """
    Check if a given number is prime.

    Args:
        n: The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Args:
        x: The number of rounds to play.
        nums: An array of integers representing the maximum value
        (n) for each round.

    Returns:
        str: The name of the player who won the most rounds
        (either 'Maria' or 'Ben'), or None if the winner cannot be determined.
    """
    if x <= 0:
        return None

    maria_turn = True
    for n in nums:
        if n < 2:
            return None  # Invalid input, so return None
        prime_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            return "Ben" if maria_turn else "Maria"
        maria_turn = not maria_turn  # Toggle the player's turn

    return "Maria" if maria_turn else "Ben"


# Test Cases
if __name__ == "__main__":
    # Test Case 1: Specific input
    x = 5
    nums = [1, 2, 3, 4, 5]
    print("Number of rounds: {}".format(x))
    print("Maximum values for each round: {}".format(nums))
    print("Winner: {}".format(isWinner(x, nums)))  # Expected output: Ben

    # Test Case 2: Specific input
    x = 10
    nums = [5, 5, 5, 5, 5, 2, 2, 2, 2, 2]
    print("Number of rounds: {}".format(x))
    print("Maximum values for each round: {}".format(nums))
    print("Winner: {}".format(isWinner(x, nums)))  # Expected output: Maria

    # Test Case 3: Handle n = 0
    x = 1
    nums = [0]
    print("Number of rounds: {}".format(x))
    print("Maximum values for each round: {}".format(nums))
    print("Winner: {}".format(isWinner(x, nums)))  # Expected output: None

    # Test Case 4: Handle negative x
    x = -1
    nums = [10]
    print("Number of rounds: {}".format(x))
    print("Maximum values for each round: {}".format(nums))
    print("Winner: {}".format(isWinner(x, nums)))  # Expected output: None

#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.
"""

from typing import List, Union


def makeChange(coins: List[int], total: int) -> Union[int, float]:
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (List[int]): List of coin values.
        total (int): The desired total amount.

    Returns:
        Union[int, float]: The fewest number of coins needed.
            If the total is 0 or less, returns 0.
            If the total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    memo = {}  # Memoization dictionary to store computed results

    def dp(target):
        if target in memo:
            return memo[target]
        if target == 0:
            return 0
        if target < 0:
            return -1

        INF = float('inf')
        min_count = INF

        for coin in coins:
            subproblem = dp(target - coin)
            if subproblem == -1:
                continue
            min_count = min(min_count, subproblem + 1)

        memo[target] = min_count if min_count != INF else -1
        return memo[target]

    result = dp(total)
    return result


if __name__ == "__main__":
    """ Example test cases """
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

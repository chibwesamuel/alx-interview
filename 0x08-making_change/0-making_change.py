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

    INF = float('inf')
    dp = [INF] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != INF else -1


if __name__ == "__main__":
    """ Example test cases """
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

#!/usr/bin/python3
"""
Function that returns fewest number of coins needed to meet total
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determine the fewest number of coins needed to meet a given amount total,
    given a pile of coins of different values.

    :param coins: List of coin values available.
    :param total: Target total to make with coins.
    :return: Fewest number of coins needed to meet total, or -1 if impossible
    """
    if total < 1:
        return 0

    # Initialize a list to store the minimum number of coins needed for each
    # value from 0 to total
    min_coins = [-1] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins needed to make a total of 0

    # Iterate through each coin value
    for coin in coins:
        # Optimize range to start from coin
        for value in range(coin, total + 1):
            # Update the minimum number of coins needed for the current total
            if min_coins[value - coin] != -1:
                if min_coins[value] == -1:
                    min_coins[value] = min_coins[value - coin] + 1
                else:
                    min_coins[value] = min(min_coins[value],
                                           min_coins[value - coin] + 1)

    # Return the minimum number of coins for the target total
    return min_coins[total]


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))

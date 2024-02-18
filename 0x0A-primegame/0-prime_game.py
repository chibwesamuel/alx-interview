#!/usr/bin/python3
"""
Determines winner of prime number removal game with optimal play.
"""


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Prototype: def isWinner(x, nums)

    Args:
        x: The number of rounds played.
        nums: An array of integers representing the value of n for each round.

    Returns:
        The name of the player who won the most rounds.
        If the winner cannot be determined, returns None.
    """
    def is_prime(n):
        """
        Check if a number is prime.

        Args:
            n: The number to check.

        Returns:
            True if the number is prime, False otherwise.
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

    def get_primes(max_num):
        """
        Get all prime numbers up to a given maximum number.

        Args:
            max_num: The maximum number.

        Returns:
            A list of prime numbers.
        """
        primes = []
        for num in range(2, max_num + 1):
            is_prime = True
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes

    def isMariaWin(primes):
        """
        Determine if Maria wins the game.

        Args:
            primes: A list of prime numbers.

        Returns:
            True if Maria wins, False otherwise.
        """
        # Count the occurrences of each prime number
        prime_counts = {}
        for p in primes:
            prime_counts[p] = prime_counts.get(p, 0) + 1

        # Determine who wins based on the count of each prime number
        maria_wins = True
        for count in prime_counts.values():
            # If the count is even, Maria will lose this round
            if count % 2 == 0:
                maria_wins = False
                break

        return maria_wins

    maria_wins_count = 0
    ben_wins_count = 0

    max_num = max(nums)  # Find the maximum value in nums

    for n in nums:
        primes = get_primes(n if n < max_num else max_num)
        maria_wins = isMariaWin(primes)

        if maria_wins:
            maria_wins_count += 1
        else:
            ben_wins_count += 1

    if maria_wins_count > ben_wins_count:
        return "Maria"
    elif ben_wins_count > maria_wins_count:
        return "Ben"
    else:
        return None
